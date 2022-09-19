from django.urls import include
from django.urls import re_path as url
from .views import ClientViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('manage', ClientViewSet, basename='clients')

urlpatterns = [
    url(r'', include(router.urls))
]
