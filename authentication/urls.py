from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('',views.home, name= "home"),
   path('signup', views.signup, name="signup"),
   path("signin", views.signin, name="signin"),
   path("logout", auth_views.LogoutView.as_view(), name='logout'),
   path("fav/<int:user_id>/", views.fav, name="fav"),
   path("addfav", views.addfav, name="addfav"),
  
]