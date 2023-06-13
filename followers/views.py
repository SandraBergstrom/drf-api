from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Followers
from .serializers import FollowerSerializer
from rest_framework.exceptions import ValidationError


class FollowerList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FollowerSerializer
    queryset = Followers.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except ValidationError as error:
            print("Validation error:", error.detail)

class FollowerDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FollowerSerializer
    queryset = Followers.objects.all()
