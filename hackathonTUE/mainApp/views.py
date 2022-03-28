from django.shortcuts import render
from django.urls import reverse
from .models import Blog, Feedback, newsFeed
from django.views.generic import View
from django.views import generic
from .forms import FeedbackForm

# Create your views here.
def home(request):
    return render(request, 'mainApp/index.html')

def about(request):
    return render(request, "mainApp/about.html")

def Community(request):
    return render(request, "mainApp/aboutCommunity.html")

def CoreValue(request):
    return render(request, "mainApp/aboutCoreValue.html")

def PeopleWithUs(request):
    return render(request, "mainApp/aboutPeopleWithUs.html")

def Blogs(request):
    blogs = Blog.objects.all()
    return render(request, "mainApp/blog.html", {'post':blogs})

# class feedback(generic.CreateView, View):
#     model = Feedback
#     form_class = FeedbackForm
#     template_name = "mainApp/feedback.html"

def feedback(request):
    post = Feedback.objects.all()
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            dweet = form.save()
            # dweet.user = request.user
            dweet.save()
    form = FeedbackForm()
    return render(request, "mainApp/feedback.html", {'form':form, 'post':post})

class BlogView(generic.DetailView, View):
    model = Blog
    template_name = 'mainApp/Blogposts.html'

def contactus(request):
    return render(request, "mainApp/ContactUs.html")

def allNews(request):
    news = newsFeed.objects.all()
    return render(request, 'mainApp/allNews.html', {'news':news})

class NewsView(generic.DetailView, View):
    model = newsFeed
    template_name = 'mainApp/NewsPost.html'