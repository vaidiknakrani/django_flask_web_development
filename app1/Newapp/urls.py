from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home_page),
    path('Newapp/',views.Newapp),
    # path('profile/',views.pr
    # ofile),
    path('',views.home)
]