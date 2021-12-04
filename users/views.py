from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer,StudentSerializer,TeacherSerializer
from .models import User,Student,Teacher
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser,IsAuthenticatedOrReadOnly



class StudentViewSet(viewsets.ModelViewSet):
	serializer_class = StudentSerializer
	queryset = Student.objects.all()
	authentication_classes = [BasicAuthentication]
	permission_classes = [IsAdminUser]

class TeacherViewSet(viewsets.ModelViewSet):
	serializer_class = TeacherSerializer
	queryset = Teacher.objects.all()
	authentication_classes = [BasicAuthentication]
	permission_classes = [IsAdminUser]

class UserViewSet(viewsets.ModelViewSet):
	serializer_class = UserSerializer
	queryset = User.objects.all()
	authentication_classes = [BasicAuthentication]
	permission_classes = [IsAdminUser]


