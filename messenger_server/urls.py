from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ApiUsers, ApiRooms

router = DefaultRouter()
router.register('rooms', ApiRooms)
router.register('users', ApiUsers)

urlpatterns = [
    path('api/', include(router.urls)),
]
