from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='index'),
    path('about',views.about,name='about'),
    path('upload',views.upload,name='upload'),
    path('result',views.upload,name='result')
]