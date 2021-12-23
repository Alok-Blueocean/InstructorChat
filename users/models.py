from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
import operator

class User(AbstractUser):
	is_student = models.BooleanField(default=False)
	is_teacher = models.BooleanField(default=False)

	# def save(self, *args, **kwargs):
		
	# 	if not operator.xor(self.is_student,self.is_teacher):
	# 	    raise ValidationError("Please mark as either teacher or Student")
	# 	else:
	# 	    super(User, self).save(*args, **kwargs)


	def __str__(self):
		return self.username

class Student(models.Model):
	# student_id = models.CharField(max_length=20)
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	def __str__(self):
		return self.user.username

	# def save(self, *args, **kwargs):
		
	# 	if not operator.xor(self.user.is_student,self.user.is_teacher):
	# 	    raise ValidationError("Please mark as either teacher or Student")
	# 	else:
	# 	    super(Student, self).save(*args, **kwargs)


class Teacher(models.Model):
	# student_id = models.CharField(max_length=20)
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	def __str__(self):
		return self.user.username