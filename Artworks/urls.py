from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . views import ArtWorks_view

router = DefaultRouter()
router.register('Artwork',ArtWorks_view)
urlpatterns = [
    path('',include(router.urls)),
]