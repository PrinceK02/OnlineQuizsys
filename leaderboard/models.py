from django.db import models
from quiz.models import quizze

from django.contrib.auth import get_user_model

User=get_user_model()
# Create your models here.



class leaderboard(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	quiz=models.ForeignKey(quizze,on_delete=models.CASCADE,null=True)
	correct_qus=models.IntegerField()
	wrong_qus=models.IntegerField()
	points=models.IntegerField()
	message=models.CharField(max_length=255)
	attempted_qus=models.IntegerField()


	def __str__(self):
		return self.user.email
