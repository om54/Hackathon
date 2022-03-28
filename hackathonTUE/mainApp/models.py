from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class newsFeed(models.Model):
	user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
	title = models.CharField(max_length=255)
	desc = models.TextField()
	date = models.DateField()
	def __str__(self):
        	return self.title + ' | ' + str(self.user)

class Blog(models.Model):
	user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
	title = models.CharField(max_length=255)
	desc = models.TextField()
	date = models.DateField(auto_now_add=True)

	def __str__(self):
        	return self.title + ' | ' + str(self.user)

class Feedback(models.Model):
	user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
	message = models.TextField()
	name = models.CharField(max_length=150, default="")

	def __str__(self):
	    return str(self.name)