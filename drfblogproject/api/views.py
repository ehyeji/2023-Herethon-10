from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .serializers import *
from .models import *
from rest_framework import views
from rest_framework.response import Response 

# Create your views here.


class PostListView(views.APIView):
    def get(self, request, format=None):
        posts=Post.objects.all()
        serializer=PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer=PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class PostDetailView(views.APIView):      
    def get(self, request, pk, format=None):
        post=get_object_or_404(Post, pk=pk)
        serializer=PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        post=get_object_or_404(Post, pk=pk)
        serializer=PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        post=get_object_or_404(Post, pk=pk)
        post.delete()
        return Response({"message":"게시물 삭제 성공"})

class CommentView(views.APIView):    
    def post(self, request, format=None):
        serializer=CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def get(self, request, format=None):
        comments=Comment.objects.all()
        serializer=CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
class CommentDetailView(views.APIView):
    def get(self, request, pk, format=None):
        comments=get_object_or_404(Comment, pk=pk)
        serializer=CommentSerializer(comments)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        comments=get_object_or_404(Comment, pk=pk)
        serializer=CommentSerializer(comments, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request, pk, format=None):
        comments=get_object_or_404(Comment, pk=pk)
        comments.delete()
        return Response({"message":"댓글 삭제 성공"})
    
class SignUpView(views.APIView):
    def post(self, request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'회원가입 성공', 'data':serializer.data})
        return Response({'message':'회원가입 실패', 'error':serializer.errors})
    
class LoginView(views.APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)

        if serializer.is_valid():
            return Response({"message":"로그인 성공", 'data':serializer.data})
        return Response({"message":"로그인 실패", 'error':serializer.errors})

# Create your views here.
