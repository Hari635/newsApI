from decimal import Context
from django.core.checks import messages
from rest_framework.generics import get_object_or_404
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Article,Journalist
from .serializers import ArticleSerilizer,JournalistSerializer

# Create your views here.

# @api_view(["GET","POST"])
# def article_list_create_api_view(request):
#     if(request.method=="GET"):
#         articles=Article.objects.filter(active=True)
#         serializer=ArticleSerilizer(articles,many=True)
#         #the serilizer take only one instance at the time to make the more instance is to add many=True
#         return Response(serializer.data)
#     elif(request.method=="POST"):
#         serializer=ArticleSerilizer(data=request.data)
#         if(serializer.is_valid()):
#             serializer.save()
#             return(Response(serializer.data,status=status.HTTP_201_CREATED))
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# @api_view(["GET","PUT","DELETE"])
# def article_detail_api_view(request,pk):
#     try:
#         article=Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return Response({"error":{
#             "code":404,
#             "messages":"Article not found"
#         }},status=status.HTTP_404_NOT_FOUND)
#     if(request.method=="GET"):
#         serializer=ArticleSerilizer(article)
#         return Response(serializer.data)
#     elif request.method=="PUT":
#         serializer=ArticleSerilizer(article,data=request.data)
#         if(serializer.is_valid()):
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     elif(request.method=="DELETE"):
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class ArticleListCreateAPIView(APIView):

    def get(self,request):
        articles=Article.objects.filter(active=True)
        serializer=ArticleSerilizer(articles,many=True)
        #the serilizer take only one instance at the time to make the more instance is to add many=True
        return Response(serializer.data)
    def post(self,request):
        serializer=ArticleSerilizer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return(Response(serializer.data,status=status.HTTP_201_CREATED))
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ArticleDetailAPIView(APIView):
    def get_object(self,pk):
        article=get_object_or_404(Article,pk=pk)
        return article
    def get(self,request,pk):
        article=self.get_object(pk)
        serializer=ArticleSerilizer(article)
        return Response(serializer.data)
    
    def put(self,request,pk):
        article=self.get_object(pk)
        serializer=ArticleSerilizer(article,data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        article=self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class JournalistListCreateAPIView(APIView):

    def get(self,request):
        journalists=Journalist.objects.all()
        serializer=JournalistSerializer(journalists,many=True,context={'request':request})
        #above serializer syntax to create hyperlink
        #the serilizer take only one instance at the time to make the more instance is to add many=True
        return Response(serializer.data)
    def post(self,request):
        serializer=JournalistSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return(Response(serializer.data,status=status.HTTP_201_CREATED))
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)