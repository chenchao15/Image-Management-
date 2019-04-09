from django.db import models
from django.utils import timezone

# Create your models here.

class Picture(models.Model):
	picture_user = models.ForeignKey('auth.User', null = True)
	picture_load = models.FileField(upload_to='upload', default = '')
	picture_name = models.CharField(max_length=50)
	picture_label = models.CharField(max_length = 50)
	picture_message = models.CharField(max_length = 100, default = " ")
	picture_time = models.DateTimeField(default=timezone.now)
	def __unicode__(self):
		return self.picture_name

class Reply(models.Model):
	post = models.ForeignKey('Picture',
		related_name = 'replies',
		related_query_name = 'reply')
	author = models.ForeignKey('auth.User')
	content = models.TextField(default=None)
	created_at = models.DateTimeField(default=timezone.now)

