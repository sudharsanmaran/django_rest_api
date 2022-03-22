
from django.shortcuts import render
from rest_framework import status, generics,mixins
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from app1.models import Snippet
from app1.serializers import SnippetSerializer
from rest_framework.authentication import SessionAuthentication,BasicAuthentication,TokenAuthentication
# Create your views here.
# fucn base view
@api_view(['GET',"POST",'DELETE','PUT'])
def snippet_list(request,pk):
    try:
        snippet=Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = Snippet.objects.all()
        serializer = SnippetSerializer(data, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT":
        serializer= SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
# tst for cmit


#generic view,inherit generic & mixins class in restframework
class GenericSnippetView(generics.GenericAPIView,
                         mixins.ListModelMixin,
                         mixins.CreateModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         mixins.RetrieveModelMixin):
    serializer_class = SnippetSerializer
    queryset = Snippet.objects.all()
    lookup_field = 'id'
    authentication_classes = [SessionAuthentication,BasicAuthentication,TokenAuthentication]
    permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]

    def get(self,request,id=None):
        if id:
            return self.retrieve(request)

        return self.list(request)

    def post(self,request,id):
        return self.create(request)

    def put(self,request,id):
        return self.update(request,id)

    def delete(self,request,id):
        return self.destroy(request,id)

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

#class view to  deal  with single instance
class SnippetDetialView(APIView):

    def get_object(self,id):
        try:
            return Response(SnippetSerializer(
                Snippet.objects.get(id=id),many=True).data)
        except Snippet.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,id):
        data=Snippet.objects.get(id=id)
        serializer=SnippetSerializer(data,many=True)
        return Response(serializer.data)

    # def post(self,request,id):
    #     data=request.data
    #     # for parse json to model instent field
    #     # use data arg in serializer model
    #     serializer=SnippetSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



