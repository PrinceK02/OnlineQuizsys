from django.db import models
from quiz.models import quizze
from django.core.validators import MinValueValidator,MaxValueValidator

from django.contrib.auth import get_user_model

User=get_user_model()

# Create your models here.



class sprofile(models.Model):
	CHOICES= [
    ('CS', 'Computer Science'),
    ('IT', 'Information Technology'),
    ('Civil', 'Civil'),
    ('Mechanical', 'Mechanical'),
    ('EC', 'Electronics & Communication'),
    ('EEE', 'Electrical & Electronics Engg.'),
    ('EE', 'Electrical Engg.'),
    ('IC', 'Instrumentation & Control Engg.'),
    ]
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	name=models.CharField(max_length=255)
	college=models.CharField(max_length=255)
	year=models.PositiveIntegerField(default=1,validators=[MinValueValidator(1),MaxValueValidator(4)])
	branch=models.CharField(max_length=255,choices=CHOICES)
	start_time=models.IntegerField(default=0)
	rem_time=models.IntegerField(default=1800)
	contact=models.CharField(null=True,blank=True,max_length=20)
	status=models.CharField(max_length=255,choices=[('Student','Student'),('Teacher','Teacher')])
	quizes=models.ManyToManyField(quizze,blank=True)

	def __str__(self):
		return self.name
