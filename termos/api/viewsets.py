from rest_framework import viewsets
from termos.api import serializers
from termos import models


class TermosViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TermosSerializer
    queryset = models.Termos.objects.all()