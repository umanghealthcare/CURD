from django.db import models

# Create your models here.
class User(models.Model):
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	address=models.TextField()
	mobile=models.CharField(max_length=14)
	gender=models.CharField(max_length=100)
	language=models.CharField(max_length=100)
	password=models.CharField(max_length=100)

	def __str__(self):
		return self.fname +'='+self.lname



