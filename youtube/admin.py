from django.contrib import admin
from youtube.models import Constant, Video, Thumbnail
# Register your models here.

admin.site.register(Constant)
admin.site.register(Video)
admin.site.register(Thumbnail)