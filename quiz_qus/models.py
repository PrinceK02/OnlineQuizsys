from django.db import models

# Create your models here.




class question(models.Model):
	qus_id=models.IntegerField(unique=True)
	title=models.CharField(max_length=255)
	desc=models.TextField()
	option_1=models.CharField(max_length=255)
	option_2=models.CharField(max_length=255)
	option_3=models.CharField(max_length=255)
	option_4=models.CharField(max_length=255)
	correct_option=models.IntegerField()

	def __str__(self):
		return self.title
