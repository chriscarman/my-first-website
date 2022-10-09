from django.db import models

class Breed(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Cat(models.Model):
    nickname = models.CharField(max_length=200)
    breed = models.ForeignKey('Breed', on_delete=models.CASCADE, null=False)
    weight = models.FloatField()
    foods = models.CharField(max_length=300, default='Birds')

    def __str__(self):
        """String for representing the Model object."""
        return self.nickname