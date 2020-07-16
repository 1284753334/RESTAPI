# 此文件为序列化器
from django.contrib.auth.models import User, Group
from rest_framework import serializers

from REST.models import Book


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        # User为系统内置
        model = User
        fields = ('url','username','email','group')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =Group
        fields = ('url','name')

# 序列化转换
class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('url','b_name','b_price')









