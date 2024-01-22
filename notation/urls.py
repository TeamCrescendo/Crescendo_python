from django.contrib import admin 
from django.urls import path 
from . import views 

urlpatterns = [ 
	path('youtube/', views.get_youtube_info, name='get_youtube_info'), 

] 