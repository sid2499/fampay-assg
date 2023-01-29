from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from fampay.responses import init_response, send_200, send_400
from .tasks import add_data_to_db
from fampay.paginator import DataPaginator
from fampay.constants import PaginationError, PaginationConstant
from fampay.exceptions import PaginationException
from .constants import VideoConstants
from .models import Video
from .serializer import VideoSerializer
from django.db.models import Q

# Create your views here.


class GetVideos(View):
    def __init__(self):
        self.response = init_response(
            response_string=VideoConstants.VIDEO_FETCH_SUCCESS_RESPONSE_MESSAGE
        )

    def get(self, request):
        try:
            request_data = request.GET
            page_number = int(
                request_data.get("page_no", PaginationConstant.PAGE_NUMBER)
            )
            limit_per_page = int(
                request_data.get("limit", PaginationConstant.LIMIT_PER_PAGE)
            )
            videos = Video.objects.all().order_by("-publishTime")
            self.response["response_data"] = DataPaginator.get_paginated_result(
                queryset=videos,
                page_number=page_number,
                limit_per_page=limit_per_page,
                serializer=VideoSerializer,
            )
            print(self.response["response_data"])
        except (ValueError, PaginationException):
            self.response[
                "response_code"
            ] = PaginationError.PAGINATION_ERROR_RESPONSE_CODE
            self.response[
                "response_string"
            ] = PaginationError.PAGINATION_ERROR_RESPONSE_MESSAGE
            return send_400(data=self.response)
        except Exception as ex:
            print(f"ISSUE OCCURRED WHILE GETTING JOB,: {ex}")
            self.response["response_code"] = VideoConstants.VIDEO_FETCH_FAILED_RESPONSE_CODE
            self.response[
                "response_string"
            ] = VideoConstants.VIDEO_FETCHED_FAILED_RESPONSE_MESSAGE
            return send_400(self.response)
        return send_200(self.response)


class SearchVideo(View):
    def __init__(self):
        self.response = init_response(
            response_string=VideoConstants.VIDEO_FETCH_SUCCESS_RESPONSE_MESSAGE
        )

    def get(self, request):
        try:
            request_data = request.GET
            page_number = int(
                request_data.get("page_no", PaginationConstant.PAGE_NUMBER)
            )
            limit_per_page = int(
                request_data.get("limit", PaginationConstant.LIMIT_PER_PAGE)
            )
            query = request_data.get("query", "").strip()
            videos = Video.objects.filter(Q(title__icontains=query) | Q(description__icontains=query)).order_by("-publishTime")
            self.response["response_data"] = DataPaginator.get_paginated_result(
                queryset=videos,
                page_number=page_number,
                limit_per_page=limit_per_page,
                serializer=VideoSerializer,
            )
        except (ValueError, PaginationException):
            self.response[
                "response_code"
            ] = PaginationError.PAGINATION_ERROR_RESPONSE_CODE
            self.response[
                "response_string"
            ] = PaginationError.PAGINATION_ERROR_RESPONSE_MESSAGE
            return send_400(data=self.response)
        except Exception as ex:
            print(f"ISSUE OCCURRED WHILE GETTING JOB,: {ex}")
            self.response["response_code"] = VideoConstants.VIDEO_SEARCH_FAILED_RESPONSE_CODE
            self.response[
                "response_string"
            ] = VideoConstants.VIDEO_SEARCH_FAILED_RESPONSE_MESSAGE
            return send_400(self.response)
        return send_200(self.response)
