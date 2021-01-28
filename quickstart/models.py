import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


class Currency(models.Model):
    currency = models.CharField(max_length=20)
    date = models.DateField(default=datetime.date.today)


    def __str__(self):
        return self.currency