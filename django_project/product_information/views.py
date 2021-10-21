from .models import Succulents
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import SucculentsSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


# Create your views here.


class SucculentDetails(APIView):
    # permission_classes = (IsAuthenticated,)


    def get(self, request):

        tasks = Succulents.objects.all()
        serializer = SucculentsSerializer(tasks, many=True)
        print(serializer.data)
        print('12321')
        return Response(serializer.data)


class SucculentCreate(APIView):
    # permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = SucculentsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        else:
            return Response('Invalid Creation')


class SucculentUpdate(APIView):
    # permission_classes = (IsAuthenticated,)

    def post(self, request, id):
        tasks = Succulents.objects.get(pk=id)
        serializer = SucculentsSerializer(tasks)

        return Response(serializer.data)


class SucculentDelete(APIView):
    # permission_classes = (IsAuthenticated,)


    def delete(self, request, pk):
        task = Succulents.objects.get(id=pk)
        task.delete()

        return Response('Item Deleted')
