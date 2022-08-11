from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import FollowViewSet

router = DefaultRouter()
router.register('users', FollowViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls.authtoken')),
    path('', include('djoser.urls')),
]
