from django.db import models

# Create your models here.

class Task(models.Model):
	name = models.CharField(max_length=200)
	start_date = models.DateTimeField()
	end_date =  models.DateTimeField()

	def __str__(self):              
		return self.name

"""
	description
	files
"""