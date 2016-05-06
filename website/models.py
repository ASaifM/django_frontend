from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Ingredient(models.Model):
	ingredient = models.CharField(max_length=100)

	def __str__(self):
		return self.ingredient
