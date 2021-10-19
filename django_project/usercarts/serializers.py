from rest_framework import serializers
from .models import Usercarts


class UsercartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usercarts
        fields = '__all__'
