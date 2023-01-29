from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path(
        "videos/",
        views.GetVideos.as_view(),
        name="videos",
    ),
    path(
        "search/",
        views.SearchVideo.as_view(),
        name="search",
    )
]