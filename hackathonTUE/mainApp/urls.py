from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("about/community/", views.Community, name="community"),
    path("about/corevalues/", views.CoreValue, name="corevalue"),
    path("about/peoplewithus/", views.PeopleWithUs, name="peoplewithus"),
    path("feedback/", views.feedback, name="feedback"),
    path("blogs/", views.Blogs, name="blogs"),
    path("blogs/blogpost/<int:pk>/", views.BlogView.as_view(), name='blogpost'),
    path("contact/", views.contactus, name="contact"),
    path("news/", views.allNews, name="all_news"),
    path("news/newsfeed/<int:pk>/", views.NewsView.as_view(), name="newspost"),
]