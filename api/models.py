from django.db import models
from users.models import Student,Teacher

class Question(models.Model):
	question = models.CharField(max_length=200,blank=False,null=False)

	def __str__(self):
		return self.question

class Answer(models.Model):
	answer = models.TextField()
	question = models.ForeignKey(Question,on_delete=models.CASCADE,
		blank=False,null=False)


class AnswerRequest(models.Model):
	question = models.ForeignKey(Question,on_delete=models.CASCADE,
		blank=False,null=False)
	student = models.ForeignKey(Student,on_delete=models.CASCADE)
	teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
	

class AnswerResponse(models.Model):
	answer = models.ForeignKey(Answer,on_delete=models.CASCADE,
		blank=False,null=False)
	student = models.ForeignKey(Student,on_delete=models.CASCADE)
	teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)



