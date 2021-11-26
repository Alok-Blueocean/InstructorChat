from django.shortcuts import render
from rest_framework import viewsets
from .models import Question,Answer,AnswerRequest,AnswerResponse
from .serializers import QuestionSerializer,AnswerSerializer,AnswerRequestSerializer,AnswerResponseSerializer

class QuestionViewSet(viewsets.ModelViewSet):
	serializer_class = QuestionSerializer
	queryset = Question.objects.all()

class AnswerViewSet(viewsets.ModelViewSet):
	serializer_class = AnswerSerializer
	queryset = Answer.objects.all()

class AnswerRequestViewSet(viewsets.ModelViewSet):
	serializer_class = AnswerRequestSerializer
	queryset = AnswerRequest.objects.all()

class AnswerResponseViewSet(viewsets.ModelViewSet):
	serializer_class = AnswerResponseSerializer
	queryset = AnswerResponse.objects.all()