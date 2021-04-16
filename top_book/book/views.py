# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer

# Create your views here.
class GetAllData(APIView):
    def get(self, request):
        query = Book.objects.all()
        serializers = BookSerializer(query , many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
