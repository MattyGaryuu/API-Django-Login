from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView, TokenBlacklistView



urlpatterns = [
   path('token/', views.loginAPI, name='token'),
   path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
   path('token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
   path('token/user/', views.UserAPI, name='token_user'),
  
]