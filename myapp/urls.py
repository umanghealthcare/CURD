from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('header/',views.header,name='header'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('forgotpassword/',views.forgotpassword,name='forgotpassword'),
    path('otp/',views.otp,name='otp'),
    path('newpassword/',views.newpassword,name='newpassword'),
    path('contact/',views.contact,name='contact'),
    path('updateprofile/<int:pk>/',views.updateprofile,name='updateprofile'),
    path('delet/<int:pk>/',views.delet,name='delet'),



]