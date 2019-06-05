from django.db import models

class Person(models.Model):
	name = models.CharField(max_length=50, null=True)
	email = models.CharField(max_length=30, null=True)
	age = models.IntegerField(null=True)
	partner = models.OneToOneField("Partner", null=True, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.name
		
class Partner(models.Model):
	name = models.CharField(max_length=50)
	email = models.CharField(max_length=30)
	age = models.IntegerField()
	
	def __str__(self):
		return self.name
