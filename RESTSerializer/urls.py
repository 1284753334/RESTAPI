from django.conf.urls import url

from RESTSerializer import views

urlpatterns=[
    url(r'^person/',views.PersonView.as_view()),
    url(r'^students/',views.StudentView.as_view()),
    url(r'^books/',views.books),
]



















