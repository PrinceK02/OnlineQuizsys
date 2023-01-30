from django.db import models
from quiz_qus.models import question
# Create your models here.


class quizze(models.Model):
	title=models.CharField(max_length=255)
	time=models.IntegerField()
	ques=models.ManyToManyField(question)

	def __str__(self):
		return self.title
