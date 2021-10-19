from django.contrib.auth.models import User
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='pk', read_only=True)
    username = serializers.SerializerMethodField()

    def get_username(self, obj):
        return obj.username

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'id']
