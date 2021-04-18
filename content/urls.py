from django.contrib import admin
from django.urls import path
from . import views

app_name = 'content'

urlpatterns = [
	path('new_guitar/', views.new_guitar, name='new_guitar'),
	path('new_pedal/', views.new_pedal, name='new_pedal'),
	path('guitar/<int:guitar_id>', views.guitar, name='guitar'),



]