from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Equation(models.Model):
	type_of_math = models.CharField(max_length=100)
	math = models.TextField()
	time_posted = models.TimeField(default=timezone.now)
	author = models.CharField(max_length=100, primary_key = True)

	def __str__(self):
		return self.type_of_math + " " + self.math + " " + self.author




