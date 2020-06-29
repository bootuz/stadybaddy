from django.urls import path
from . import views as app_views

urlpatterns = [
    path('', app_views.index, name='index'),
    path('group/<slug:slug>', app_views.announcement, name='group'),
]