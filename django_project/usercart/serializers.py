from rest_framework import serializers
from .models import Usercart


class UsercartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usercart
        fields = ('user', 'product', 'quantity', 'total_price')
