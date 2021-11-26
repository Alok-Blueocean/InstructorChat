from rest_framework import serializers
from .models import User,Student,Teacher

class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields = ('user',)#name', 'password','email')

class TeacherSerializer(serializers.ModelSerializer):
	class Meta:
		model = Teacher
		fields = ('user',)#('username', 'password','email')

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username', 'password','email','is_student','is_teacher')