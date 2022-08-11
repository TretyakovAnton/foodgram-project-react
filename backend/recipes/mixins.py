from djoser.views import UserViewSet
from rest_framework.viewsets import ModelViewSet

from .pagination import PageLimitPagination


class CustomUserMixin(UserViewSet):
    pagination_class = PageLimitPagination


class CustomModelViewSet(ModelViewSet):
    pagination_class = PageLimitPagination
