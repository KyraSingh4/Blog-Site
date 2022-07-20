from django.db import models
from django.utils import timezone # makes default work so you can change the date 
from django.contrib.auth.models import User # allows users to author posts 
from django.urls import reverse

class Post(models.Model):
	title = models.CharField(max_length = 100)
	content = models.TextField()
	date_posted = models.DateTimeField(default = timezone.now) # auto_add changes date to last modified - auto_now_add changes date to when created
	author = models.ForeignKey(User, on_delete = models.CASCADE) # If user who created post was deleted, delete the post

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk':self.pk})