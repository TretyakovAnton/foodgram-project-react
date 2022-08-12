from rest_framework.viewsets import ModelViewSet

from .pagination import PageLimitPagination


class PaginatorMixin(ModelViewSet):
    pagination_class = PageLimitPagination
