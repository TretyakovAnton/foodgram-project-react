from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from recipes.mixins import CustomUserMixin
from .models import Follow, User
from .serializers import FollowListSerializer, FollowSerializer


class FollowViewSet(CustomUserMixin):
    queryset = User.objects.all()
    serializer_class = FollowListSerializer

    @action(detail=True,
            methods=["POST", "DELETE"],
            permission_classes=[IsAuthenticated])
    def subscribe(self, request, id):
        if request.method == "POST":
            data = {'user': request.user.id, 'following': id}
            serializer = FollowSerializer(
                data=data,
                context={'request': request}
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        user = request.user
        following = get_object_or_404(User, id=id)
        follow = get_object_or_404(Follow, user=user, following=following)
        follow.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False,
            methods=["GET"],
            permission_classes=[IsAuthenticated])
    def subscriptions(self, request):
        user = self.request.user
        queryset = User.objects.filter(following__user=user)
        serializer = self.get_serializer(
            queryset,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)
