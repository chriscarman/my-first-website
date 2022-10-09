from django.db import models

# Create your models here.

from django.db import models
from django.core.validators import MinLengthValidator


class Auto(models.Model):
    nickname = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Nickname must be greater than 1 character")]
    )
    mileage = models.PositiveIntegerField()
    purchase_date = models.DateField()

    # Shows up in the admin list
    def __str__(self):
        return self.nickname