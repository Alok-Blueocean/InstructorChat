from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer,StudentSerializer,TeacherSerializer
from .models import User,Student,Teacher

class StudentViewSet(viewsets.ModelViewSet):
	serializer_class = StudentSerializer
	queryset = Student.objects.all()

class TeacherViewSet(viewsets.ModelViewSet):
	serializer_class = TeacherSerializer
	queryset = Teacher.objects.all()

class UserViewSet(viewsets.ModelViewSet):
	serializer_class = UserSerializer
	queryset = User.objects.all()


