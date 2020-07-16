from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from App.models import Book


class HelloView(View):
    def get(self,request):
        return render(request, 'hello.html')


class HelloTemplateView(TemplateView):

    template_name= 'hello.html'


class HelloListView(ListView):
    template_name = 'Book_list.html'
    model = Book


class Hellodetail(DetailView):
    # template_name = 'BOOK.html'
    # model = Book
    # 或者 换种方式
    queryset = Book.objects.all()





