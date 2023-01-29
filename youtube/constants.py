class ApiConstants:
    API_KEYS = ['AIzaSyBlqk5hI_Qcu36BhSDIi0CZOovupTWc2HA', 'AIzaSyAq7H2UFyGgMwEUK3oHEkyeDwlDpB6JHpU', 'AIzaSyD5yLsj0SZYSXM_HLmrn_k61EvLCACUnuk']
    YOUTUBE_DATA_BASE_URL = 'https://www.googleapis.com/youtube/v3/search'
    TOPIC_ID = '/m/06ntj'     # genre: sports
    TYPE = 'video'
    PART_VALUE = 'snippet'
    ORDER = 'date'
    RELEVENT_LANG = 'en'
    MAX_RESULTS = 30

MAX_RETRY = 3


class VideoConstants:
    VIDEO_FETCH_SUCCESS_RESPONSE_MESSAGE = "Videos fetched successfully"
    VIDEO_FETCH_FAILED_RESPONSE_CODE = 20
    VIDEO_FETCHED_FAILED_RESPONSE_MESSAGE = "Video fetch failed"
    VIDEO_SEARCH_FAILED_RESPONSE_CODE = 21
    VIDEO_SEARCH_FAILED_RESPONSE_MESSAGE = "Video search failed"
