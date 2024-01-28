from django.db import models

#name, population, language, capital

# Create your models here.
class State(models.Model):
    name=models.CharField(max_length=30)
    population=models.PositiveIntegerField()
    language=models.CharField(max_length=30)
    capital=models.CharField(max_length=30)

    def __str__(self):
        return self.name
