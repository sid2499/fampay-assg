from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage
from fampay.exceptions import PaginationException


class DataPaginator:
    @staticmethod
    def get_paginated_result(
        queryset, page_number, limit_per_page, serializer=None, serializer_context=None
    ):
        try:
            paginator = Paginator(queryset, limit_per_page)
            page_object = paginator.page(page_number)
            paginated_data = page_object.object_list
            if serializer:
                paginated_data = serializer(
                    paginated_data, context=serializer_context, many=True
                ).data
        except (TypeError, InvalidPage, PageNotAnInteger, EmptyPage) as ex:
            raise PaginationException
        total_number_of_pages = paginator.num_pages
        total_number_of_items = paginator.count
        has_next_page = page_object.has_next()
        has_previous_page = page_object.has_previous()
        next_page_number = None
        previous_page_number = None
        if has_next_page:
            next_page_number = page_object.next_page_number()
        if has_previous_page:
            previous_page_number = page_object.previous_page_number()
        items_per_page = min(limit_per_page, paginator.count)
        paginated_result = {
            "pagination": {
                "total_number_of_pages": total_number_of_pages,
                "total_number_of_items": total_number_of_items,
                "has_next_page": has_next_page,
                "has_previous_page": has_previous_page,
                "next_page_number": next_page_number,
                "previous_page_number": previous_page_number,
                "page_number": page_number,
                "items_per_page": items_per_page,
            },
            "results": paginated_data,
        }
        return paginated_result
