from django.contrib import admin
from mainApp.models import Blog, Feedback, newsFeed

# Register your models here.
admin.site.register(newsFeed)

admin.site.register(Feedback)

admin.site.register(Blog)