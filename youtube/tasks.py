from celery import shared_task
import requests
from .constants import ApiConstants, MAX_RETRY
from datetime import datetime,timedelta
from .models import Constant, Video, Thumbnail
from django.utils import timezone


@shared_task(bind=True)
def add_data_to_db(self, published_after=[], published_before=[], retry=0):
    api_key_index, created = Constant.objects.get_or_create(name="current-api-key-index", defaults={"value": '0'})
    current_time = datetime.now()
    if not published_after:
        published_after = str(current_time-timedelta(hours=24)).split()
    if not published_before:
        published_before = str(current_time-timedelta(hours=24)+timedelta(seconds=30)).split()

    params = {
        'key': ApiConstants.API_KEYS[int(api_key_index.value)],
        'type': ApiConstants.TYPE,
        'maxResults': ApiConstants.MAX_RESULTS,
        'publishedAfter': published_after[0]+'T'+published_after[1]+'Z',
        'publishedBefore': published_before[0]+'T'+published_before[1]+'Z',
        'topicId': ApiConstants.TOPIC_ID,
        'part': ApiConstants.PART_VALUE,
        'relevanceLanguage': ApiConstants.RELEVENT_LANG,
        'order': ApiConstants.ORDER,
    }
    response = requests.get(ApiConstants.YOUTUBE_DATA_BASE_URL, params=params)
    if response.status_code == 200:
        videos = response.json().get('items')
        video_list = []
        thumbnail_list = []
        for video in videos:
            new_video = Video(id=video.get("id").get("videoId"), title=video.get("snippet").get("title"), description=video.get("snippet").get("description"), publishTime=timezone.make_aware(datetime.strptime(video.get("snippet").get("publishedAt"), "%Y-%m-%dT%H:%M:%SZ"), timezone.get_current_timezone()), channelId=video.get("snippet").get("channelId"), channelTitle=video.get("snippet").get("channelTitle"))
            video_list.append(new_video)
            for resolution, value in video.get("snippet").get("thumbnails").items():
                thumbnail_list.append(Thumbnail(video=new_video, resolution=resolution, url=value.get('url'), width=value.get('width'), height=value.get('height')))
        Video.objects.bulk_create(video_list)
        Thumbnail.objects.bulk_create(thumbnail_list)
    elif response.status_code == 403:
        api_key_index.value = str(int(api_key_index.value)+1)
        api_key_index.save()
        if retry < MAX_RETRY:
            self.retry(
                args=(),
                kwargs={'published_after': published_after, 'published_before': published_before, 'retry': retry + 1}
            )
    else:
        print(response.json())
        if retry < MAX_RETRY:
            self.retry(
                args=(),
                kwargs={'published_after': published_after, 'published_before': published_before, 'retry': retry+1}
            )
