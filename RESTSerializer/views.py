from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from RESTSerializer.models import Person, Student
from RESTSerializer.serializers import PersonSerializer, StudentSerializer, BookSerializer


class PersonView(View):
    def get(self,request):
        # 列表序列化
        persons = Person.objects.all()

        person_serialize = PersonSerializer(persons, many=True)

        return JsonResponse(person_serialize.data, safe=False)


    def post(self, request):
        p_name = request.POST.get('p_name')
        p_age = request.POST.get('p_age')

        person = Person()
        person.p_name = p_name
        person.p_age = p_age

        person.save()
        # 序列化出来
        person_serializer = PersonSerializer(person)



        return JsonResponse(person_serializer.data)


class StudentView(APIView):
    def post(self,request):
        #  一
        # s_name = request.POST.get('s_name')
        # s_age = request.POST.get('s_age')
        #
        # student = Student()
        #
        # student.s_name = s_name
        # student.s_age = s_age
        #
        # student.save()
        #
        # student_serialize = StudentSerializer(student)
        # data = student_serialize.data

        # return JsonResponse(data)

        #  下面简化一下
        #  data = JSONParser().parse(request)
        # print(data)
        print(type(request))

        print(type(request._request))

        print(request.GET)


        return Response({'msg':'ok'})

@api_view(http_method_names=['GET','POST'])
def books(request):
    print(type(request))

    if request.method =='GET':
        return  Response(data={'msg':'666'})
    elif request.method == 'POST':
        print(request.data)
        book_serializer = BookSerializer(data =request.data)
        if book_serializer.is_valid():
            book_serializer.save()

            return JsonResponse(book_serializer.data)
        return JsonResponse({'msg':'error'},status=400)