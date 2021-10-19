from django.shortcuts import render

# Create your views here.
from .models import PurchaseHistory
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PurchaseHistorySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


# Create your views here.


class PurchaseList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        tasks = PurchaseHistory.objects.all()
        serializer = PurchaseHistorySerializer(tasks, many=True)

        return Response(serializer.data)


class PurchaseDetails(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        tasks = PurchaseHistory.objects.get(id=pk)
        serializer = PurchaseHistorySerializer(tasks, many=True)

        return Response(serializer.data)


class PurchaseCreate(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = PurchaseHistorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        else:
            return Response('Invalid Creation')


class PurchaseDelete(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, pk):
        task = PurchaseHistory.objects.get(id=pk)
        task.delete()

        return Response('Item Deleted')
