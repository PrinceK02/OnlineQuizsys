from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth import get_user_model

User=get_user_model()

# Create your models here.

class tprofile(models.Model):
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
	branch=models.CharField(max_length=255,choices=CHOICES,default=True)
	year=models.PositiveIntegerField(default=1,validators=[MinValueValidator(1),MaxValueValidator(4)])
	contact=models.CharField(null=True,blank=True,max_length=10)
	status=models.CharField(max_length=255,choices=[('Student','Student'),('Teacher','Teacher')])

	def __str__(self):
		return self.name
