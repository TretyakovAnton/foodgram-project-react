from rest_framework import status
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from recipes.pagination import PageLimitPagination
from .models import Follow, User
from .serializers import FollowListSerializer, FollowSerializer


class FollowView(APIView):
    """
    APIView для добавления и удаления подписки на автора
    """
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageLimitPagination

    def post(self, request, id):
        data = {'user': request.user.id, 'following': id}
        serializer = FollowSerializer(data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, id):
        user = request.user
        following = get_object_or_404(User, id=id)
        follow = get_object_or_404(Follow, user=user, following=following)
        follow.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FollowListView(ListAPIView):
    """
    APIView для просмотра подписок пользователя.
    """
    serializer_class = FollowListSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageLimitPagination

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(following__user=user)
