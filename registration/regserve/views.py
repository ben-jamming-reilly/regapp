from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializers import *
from django.views.generic import ListView, CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView


def index(request):
    return HttpResponse("Hello from django backend")


class StudentListCreate(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentListForm(ListView):
    model = Student

# CRUD for student


class StudentCreateForm(CreateView, ListView):
    model = Student
    fields = ['firstname', 'lastname',
              'idnumber', 'schoolyear', 'major', 'gpa']


class StudentReadView(DetailView):
    model = Student
    fields = ['firstname', 'lastname',
              'idnumber', 'schoolyear', 'major', 'gpa']


class StudentUpdateForm(UpdateView):
    model = Student
    fields = ['firstname', 'lastname',
              'idnumber', 'schoolyear', 'major', 'gpa']
    success_url = "/regserve/students/"


class StudentDeleteForm(DeleteView):
    model = Student
    success_url = "/regserve/students/"
