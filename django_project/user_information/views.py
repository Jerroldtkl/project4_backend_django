from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProfileSerializer
from django.contrib.auth.models import User
from .models import Profile
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


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


class ProfileCreate(APIView):
    # permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = ProfileSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        else:
            return Response('Invalid Creation')


class ProfileList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        tasks = User.objects.all()
        serializer = ProfileSerializer(tasks, many=True)

        return Response(serializer.data)


class ProfileDetails(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, user_id):
        tasks = Profile.objects.all(pk=user_id)
        serializer = ProfileSerializer(tasks, many=True)

        return Response(serializer.data)


class ProfileUpdate(APIView):
    permission_classes = (IsAuthenticated,)

    def update_profile(self, request, user_id):
        tasks = Profile.objects.get(pk=user_id)
        serializer = ProfileSerializer(instance=tasks, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
