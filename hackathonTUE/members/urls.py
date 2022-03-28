from django.urls import path
from . import views

urlpatterns = [
	path("signup/", views.UserRegisterView.as_view(), name="signup")
]