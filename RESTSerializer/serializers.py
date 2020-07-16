
from rest_framework import serializers

from RESTSerializer.models import Person, Student, Book


#  原生序列化  代码比person 多
class PersonSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    p_name = serializers.CharField(max_length=32)
    p_age = serializers.IntegerField(default=1)
    P_sex = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return Person.objects.create(**validated_data)

    def update(self, instance, validated_data):
       #   如果拿不到值，就用原来的值
       instance.p_name = validated_data.get('p_name',instance.p_name)
       instance.p_age = validated_data.get('p_age',instance.p_age)
       instance.p_sex = validated_data.get('p_sex',instance.p_sex)
       instance.save()

       return instance

# 模型序列化 ModelSerializer
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        #模型序列化 不带括号
        model = Student
        fields = ('s_name','s_age')



class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('b_price','b_name')




