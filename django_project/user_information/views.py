from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProfileSerializer, RegisterSerializer
from django.contrib.auth.models import User
from .models import Profile
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status


class JWTDetails(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        response = JWTAuthentication().authenticate(request)
        if response:
            user, token = response

            print(user)
            print(user.username)
            print(user.id)
            print(user.first_name)
            print(user.last_name)

            return Response(token.payload)


class UserCreate(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        # print('data:', request.data)
        serializer = RegisterSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        tasks = User.objects.all()
        serializer = RegisterSerializer(tasks, many=True)

        return Response(serializer.data)


class ProfileDetails(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, id):
        tasks = User.objects.get(pk=id)
        serializer = RegisterSerializer(tasks)

        return Response(serializer.data)


class ProfileUpdate(APIView):
    permission_classes = (IsAuthenticated,)

    def update_profile(self, request, user_id):
        tasks = Profile.objects.get(pk=user_id)
        serializer = RegisterSerializer(instance=tasks, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
