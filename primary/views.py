from rest_framework.response import Response
from .models import Post,PostImage,Review,Reply
from .serializers import PostSerializer,PostImageSerializer,ReviewSerializer,ReplySerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import permissions 
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework import status
from .permissions import *


class PostImageViewSet(ModelViewSet):
    http_method_names=['get','options','head','get','post']
    serializer_class=PostImageSerializer
    def get_queryset(self):
       return PostImage.objects.filter(post_id=self.kwargs['post_pk'])
    
    def get_serializer_context(self):
        return {'post_id':self.kwargs['post_pk']}


class PostViewset(ModelViewSet):
    http_method_names=['get','options','head','get','post','delete']
    queryset=Post.objects.prefetch_related('image').all()
    serializer_class=PostSerializer
    permission_classes=[IsUserOrAdminDeletePermission]
    def get_serializer_context(self):
        return {'user_id':self.request.user.id}


class UserPostViewset(ModelViewSet):
    http_method_names=['get','options','head','get','post','delete']
    serializer_class=PostSerializer
    permission_classes=[IsAuthenticated,IsUserOrAdminDeletePermission]
    

    def get_queryset(self):
        user_id = self.request.user.id
        queryset = Post.objects.filter(user_id=user_id).prefetch_related('image')
        return queryset
    
    def get_serializer_context(self):
        return {'user_id':self.request.user.id}
    

class ReviewViewSet(ModelViewSet):
    http_method_names=['get','options','head','get','post','delete']
    serializer_class=ReviewSerializer
    permission_classes=[IsAuthenticated,IsUserOrAdminDeletePermission]
    

    def get_queryset(self):
        return Review.objects.filter(post_id=self.kwargs['post_pk']).select_related('user')
    
    def get_serializer_context(self):
        user_id = self.request.user.id
        return {'post_id':self.kwargs['post_pk'],'user_id':user_id}
 
    

class ReplyViewSet(ModelViewSet):
    http_method_names=['get','options','head','get','post','delete']
    serializer_class=ReplySerializer
    permission_classes=[IsAuthenticated,IsUserOrAdminDeletePermission]


    def get_queryset(self):
        review_id=self.kwargs['review_reply_pk']
        return Reply.objects.filter(review_id=review_id).select_related('user')

    def get_serializer_context(self):
        user_id = self.request.user.id
        review_id = self.kwargs['review_reply_pk']
        return {'user_id':user_id,'review_id':review_id}


    
    

