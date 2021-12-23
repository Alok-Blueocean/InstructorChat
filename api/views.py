from django.shortcuts import render
from rest_framework import viewsets
from drf_yasg.utils import no_body, swagger_auto_schema
from rest_framework.decorators import action
from .models import Question,Answer,AnswerRequest,AnswerResponse
from users.models import Student,Teacher
from .serializers import QuestionSerializer,AnswerSerializer,AnswerRequestSerializer,AnswerResponseSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser,IsAuthenticatedOrReadOnly

class QuestionViewSet(viewsets.ModelViewSet):
	serializer_class = QuestionSerializer
	queryset = Question.objects.all()
	authentication_classes = [SessionAuthentication]
	permission_classes = [IsAdminUser]

class AnswerViewSet(viewsets.ModelViewSet):
	serializer_class = AnswerSerializer
	queryset = Answer.objects.all()
	authentication_classes = [SessionAuthentication]
	permission_classes = [IsAdminUser]

class AnswerRequestViewSet(viewsets.ModelViewSet):

	serializer_class = AnswerRequestSerializer
	queryset = AnswerRequest.objects.all()
	# authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]
	
	def perform_create(self, serializer):
		raw_data = self.request.data
		question_text = raw_data.pop('question')
		question = Question(question=question_text.pop('question'))
		question.save()
		student = Student.objects.get(id=raw_data.pop('student'))
		teacher = Teacher.objects.get(id=raw_data.pop('teacher'))
		serializer.save(question=question,student=student,teacher=teacher)

class AnswerResponseViewSet(viewsets.ModelViewSet):

	serializer_class = AnswerResponseSerializer
	queryset = AnswerResponse.objects.all()
	authentication_classes = [SessionAuthentication]
	permission_classes = [IsAuthenticatedOrReadOnly]

	def perform_create(self, serializer):
		raw_data = self.request.data
		print(raw_data)
		answer_request_id = raw_data.get('answer_request')
		answer_request = AnswerRequest.objects.get(id=answer_request_id)
		question = Question.objects.get(id=answer_request.question.id)
		answer_json = raw_data.pop('answer')
		answer = Answer(answer=answer_json.pop('answer'),
			question=question)
		answer.save()
		student = Student.objects.get(id=raw_data.pop('student'))
		teacher = Teacher.objects.get(id=raw_data.pop('teacher'))
		serializer.save(answer_request=answer_request,answer=answer,student=student,teacher=teacher)