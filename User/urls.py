from rest_framework.routers import DefaultRouter
from django.urls import path,include
from . views import User_Registration,activate,User_login,User_logout_view

router = DefaultRouter()

urlpatterns = [
    path('',include(router.urls)),
    path('register/',User_Registration.as_view(),name='register'),
    path('active/<uid64>/<token>/',activate,name='activate'),
    path('login/',User_login.as_view(),name='login'),
    path('logout/',User_logout_view.as_view(),name='logout'),
]
