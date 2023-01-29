from django.db import models

# Create your models here.


class Video(models.Model):
    id = models.CharField(max_length=30, primary_key=True)
    title = models.CharField(max_length=200, db_index=True)
    description = models.TextField(db_index=True)
    publishTime = models.DateTimeField(db_index=True)
    channelTitle = models.CharField(max_length=200)
    channelId = models.CharField(max_length=50)

    def __str__(self):
        return self.title



class Thumbnail(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='thumbnails')
    url = models.URLField()
    width = models.IntegerField()
    height = models.IntegerField()
    resolution = models.CharField(max_length=50)

    def __str__(self):
        return self.url


class Constant(models.Model):
    name = models.CharField(max_length=50, unique=True)
    value = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name}"

