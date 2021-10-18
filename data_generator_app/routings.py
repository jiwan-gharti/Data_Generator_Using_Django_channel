from django.urls import path
from .consumers import DataGenerator

ws_urlpatterns = [
    path("ws/data_generator/", DataGenerator)
]

