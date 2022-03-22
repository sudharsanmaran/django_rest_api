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
#

#class based api views

class Snippet(APIView):

    def get(self,request):
        pass