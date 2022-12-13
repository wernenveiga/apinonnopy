from rest_framework import viewsets
from posts.api import serializers
from posts import models


class PostsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PostSerializer
    queryset = models.Posts.objects.all()