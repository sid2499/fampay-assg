from celery import shared_task
import requests
from .constants import ApiConstants
from datetime import datetime,timedelta


@shared_task(bind=True)
def test_func(self):
    publishedAfter = str(datetime.now()-timedelta(hours=24)).split()
    params = {
        'key': ApiConstants.API_KEYS[0],
        'type': ApiConstants.TYPE,
        'maxResults': ApiConstants.MAX_RESULTS,
        'publishedAfter': publishedAfter[0]+'T'+publishedAfter[1]+'Z',
        'topicId': ApiConstants.TOPIC_ID,
        'part': ApiConstants.PART_VALUE,
        'relevanceLanguage': ApiConstants.RELEVENT_LANG,
        'order': ApiConstants.ORDER,
    }
    headers = {"Accept": "application/json"}
    response = requests.get(ApiConstants.YOUTUBE_DATA_BASE_URL, params=params)
    print(response.json())
    return 'Done' 