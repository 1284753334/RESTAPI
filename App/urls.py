from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from App import views

app_name = 'app'
urlpatterns = [
    url(r'^hello/',views.HelloView.as_view(),name='hello'),
    url(r'^template/',views.HelloTemplateView.as_view(),name='template'),
    url(r'^listview/',views.HelloListView.as_view(),name='listview'),
    url(r'^single/(?P<pk>\d+)/',views.Hellodetail.as_view(),name='single'),
]