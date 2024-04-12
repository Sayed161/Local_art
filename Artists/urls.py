from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . views import Artists_View

router = DefaultRouter()
router.register('Artists',Artists_View)
urlpatterns = [
    path('',include(router.urls)),
]