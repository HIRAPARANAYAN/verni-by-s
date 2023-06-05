from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.login,name='loginform'),
    # path('OTP/',views.otp,name="otp"),
    path('verifyotp/',views.verifyotp,name='verifyotp'),
    path('multiform/',views.multiform,name='multiform'),
    path("payment_index/", views.payment_home, name="payment_home"),
    path("payment/", views.order_payment, name="payment"),
    path("callback/", views.callback, name="callback"),
]