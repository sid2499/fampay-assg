from rest_framework import serializers
from youtube.models import Thumbnail, Video


class ThumbnailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thumbnail
        fields = ('resolution', 'url', 'width', 'height')


class VideoSerializer(serializers.ModelSerializer):
    thumbnails = serializers.SerializerMethodField()

    def get_thumbnails(self, video):
        video_thumbnails = video.thumbnails.all()
        return ThumbnailSerializer(video_thumbnails, many=True)

    class Meta:
        model = Video
        fields = ('id', 'title', 'description', 'publishTime', 'channelTitle', 'channelId', 'thumbnails')