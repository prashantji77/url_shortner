from django.urls import path
from . import views
from shortUrl.views import *

urlpatterns = [
    path('',views.home),
    path('create',views.createShortUrl),
    path('<str:shorturl>',views.redirectUrl)
]
