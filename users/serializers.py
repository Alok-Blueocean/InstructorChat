from rest_framework import serializers
from .models import User,Student,Teacher



class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username', 'password','email','is_student','is_teacher')

class StudentSerializer(serializers.HyperlinkedModelSerializer):
	user = UserSerializer(many=False,read_only=True)
	class Meta:
		model = Student
		fields = ('user',)#name', 'password','email')

class TeacherSerializer(serializers.ModelSerializer):
	class Meta:
		model = Teacher
		fields = ('user',)#('username', 'password','email')