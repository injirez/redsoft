from django.urls import path
from .views import WeatherAPIView


urlpatterns = [
    path(r'<str:city>/<str:date>', WeatherAPIView.as_view(), name='weather'),
]