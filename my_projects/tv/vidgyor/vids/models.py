# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import timedelta
from django.db import models

# Create your models here.
class Video(models.Model):
    title= models.CharField(primary_key=True,max_length=255)
    name = models.CharField(max_length=500, null=True, blank=True)
    video_id = models.IntegerField(default=1)
    description=models.CharField(max_length=500,null=True, blank=True)
    #video_id =
    #thumbnail=
    #video_type=
    categories=models.CharField(max_length=500,null=True, blank=True)
    tags=models.CharField(max_length=500,null=True, blank=True)
    #plays=
    #status=

    videofile= models.FileField(unique=True,upload_to='videos/', null=True, verbose_name="")
    def save(self, *args, **kwargs):
        # This means that the model isn't saved to the database yet
        if self._state.adding:
            # Get the maximum display_id value from the database
            last_id = Video.objects.all().aggregate(largest=models.Max('video_id'))['largest']

            # aggregate can return None! Check it first.
            # If it isn't none, just use the last ID specified (which should be the greatest) and add one to it
            if last_id is not None:
                self.video_id = last_id + 1

        super(Video, self).save(*args, **kwargs)
#
    #def __str__(self):
    #    return str(self.videofile)
class VideoMetadata(models.Model):
    meta_title = models.ForeignKey(Video, on_delete=models.CASCADE)
    created_on=models.DateTimeField(auto_now_add=True, blank=True)
    duration=models.CharField(max_length=500)#models.DurationField(default=timedelta())


class TempVal(models.Model):
    temp_val=models.CharField(max_length=500)
