from rest_framework import serializers
from .models import Succulents


class SucculentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Succulents
        fields = '__all__'
