from django.contrib import admin 
from django.urls import path 
from . import views 

urlpatterns = [ 
	path('ai/', views.get_ai_info, name='get_ai_info'), 

] 