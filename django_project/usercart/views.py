from .models import Usercart
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UsercartSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.


class UsercartDetails(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        tasks = Usercart.objects.get(id=pk)
        serializer = UsercartSerializer(tasks, many=True)

        return Response(serializer.data)


class UsercartCreate(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        response = JWTAuthentication().authenticate(request)
        if response:
            user, token = response
            request.data.id = user.id

        serializer = UsercartSerializer(data=request.data)
        print(serializer.is_valid())
        print(serializer)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        else:
            return Response(serializer.errors)


class UsercartUpdate(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk):
        tasks = Usercart.objects.get(id=pk)
        serializer = UsercartSerializer(instance=tasks, data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)


class UsercartDelete(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, pk):
        task = Usercart.objects.get(id=pk)
        task.delete()

        return Response('Item Deleted')
