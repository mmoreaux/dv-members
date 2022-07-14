from django.urls import path

from . import views

urlpatterns = [
	path('mems', views.mems, name='mems'),
]
