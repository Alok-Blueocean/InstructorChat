from .models import Question,Answer,AnswerRequest,AnswerResponse
from rest_framework import serializers

class QuestionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Question
		fields = ('question',)

class AnswerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Answer
		fields = ('answer',)

class AnswerRequestSerializer(serializers.ModelSerializer):
	question = QuestionSerializer(many=False)
	class Meta:
		model = AnswerRequest
		fields = ('question','student','teacher')

class AnswerResponseSerializer(serializers.ModelSerializer):
	answer = AnswerSerializer(many=False)
	class Meta:
		model = AnswerResponse
		fields = '__all__'