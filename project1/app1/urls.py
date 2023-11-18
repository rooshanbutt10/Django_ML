from django.urls import path
from . import views 

urlpatterns = [
    path("", views.welcome, name='welcome'),
    path("aboutme/", views.aboutme_fun, name='aboutme'),
    path("contactus/", views.contactus_fun, name='contactus'),

]
