from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.CustomerDashboard,name='CustomerDashboard'),
    path('MyProfile/',views.MyProfile,name='MyProfile'),
    path('KYCDocument/',views.KYCDocument,name='KYCDocument'),
]