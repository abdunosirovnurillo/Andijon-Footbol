from django.urls import path
from .views import *


urlpatterns = [
    path('get-info/', get_info),
    path('get-main/', get_main),
    path('get-media/', get_media),
    path('get-news/', get_news),
    path('get-shop/', get_shop),
    path('get-about/', get_about),
    path('get-statistic/', get_statistic),
    path('get-players/', get_players)
]