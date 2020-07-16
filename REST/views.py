from django.shortcuts import render

from django.conf.urls import url, include
from django.contrib.auth.models import User, Group
from rest_framework import routers, serializers, viewsets

from REST.models import Book
from REST.serializers import UserSerializer, GroupSerializer, BookSerializer


class UserViewSet(viewsets.ModelViewSet):
    # 数据序列化
    queryset = User.objects.all()
    # 序列化类  缺点  太多 手动太慢
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer



class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


