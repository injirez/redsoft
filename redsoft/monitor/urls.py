from django.urls import path
from .views import MemoryAPIView

urlpatterns = [
    path('memory/', MemoryAPIView.as_view(), name='memory'),
]