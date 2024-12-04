from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, UserCreateViewSet


app_name = 'users'
router = DefaultRouter()
router.register('user_create', UserCreateViewSet, basename='user_create')
router.register('users', UserViewSet, basename='users')


urlpatterns = [
    path('', include(router.urls))
]
