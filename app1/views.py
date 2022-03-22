from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from app1.models import Snippet
from app1.serializers import SnippetSerializer

# Create your views here.
# @api_view(['GET',"POST",'DELETE','PUT'])
# def snippet_list(request,pk):
#     try:
#         snippet=Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         data = Snippet.objects.all()
#         serializer = SnippetSerializer(data, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == "DELETE":
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     elif request.method == "PUT":
#         serializer= SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
# tst for cmit

#class based api views

class SnippetView(APIView):

    def get(self,request):
        data=Snippet.objects.all()
        print(data)
        serializer=SnippetSerializer(data,many=True)
        return Response(serializer.data)

    def post(self,request):
        data=request.data
        # for parse json to model instent field
        # use data arg in serializer model
        serializer=SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request):
        data=request.data

    # check to set specific url to this func for single get
    # def get_one(self,request,pk):
    #     data=Snippet.objects.filter(id=pk)
    #     print(data)
    #     serialiazer=SnippetSerializer(data,many=True)
    #     return Response(serialiazer.data)