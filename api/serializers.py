from .models import Question,Answer,AnswerRequest,AnswerResponse
from rest_framework import serializers

class QuestionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Question
		fields = ('question',)

class AnswerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Answer
		fields = ('question','answer')

class AnswerRequestSerializer(serializers.ModelSerializer):
	class Meta:
		model = AnswerRequest
		fields = ('question','student','teacher')

class AnswerResponseSerializer(serializers.ModelSerializer):
	class Meta:
		model = AnswerResponse
		fields = ('answer','student','teacher')