from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Equation(models.Model):
	type_of_math = models.CharField(max_length=15)	
	math = models.TextField(max_length=100)
	time_posted = models.TimeField(default=timezone.now())
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	






