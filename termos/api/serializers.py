from rest_framework import serializers
from termos import models


class TermosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Termos
        fields = '__all__'