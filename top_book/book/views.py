from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer

# Create your views here.
class GetAllData(APIView):
    def get(self, request):
        query = Book.objects.all().order_by('-create_at')
        serializers = BookSerializer(query , many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def allApi(request):
    if request.method == 'GET':
        query = Book.objects.all().order_by('-create_at')
        serializer = BookSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def SetData(request):
    if request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATE)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


class GetFavData(APIView):
    def get(self,request):
        query = Book.objects.filter(fav=True)
        serializer = BookSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateFavData(APIView):
    def get(self, request, pk):
        query = Book.objects.get(pk=pk)
        serializer = BookSerializer(query)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        query = Book.objects.get(pk=pk)
        serializer = BookSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:    
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostModelData(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SearchData(APIView):
    def get(self, request):
        search = request.GET['name']
        query = Book.objects.filter(store_name__contains=search)
        serializer= BookSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DeleteData(APIView):
    def delete(self, request, pk):        
        query = Book.objects.get(pk=pk)
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)