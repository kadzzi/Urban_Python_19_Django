from django.db import models


# Create your models here.
class Bayer(models.Model):
    name = models.CharField(max_length=30)
    balance = models.DecimalField(max_digits=6, decimal_places=2)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Bayer)

    def __str__(self):
        return self.title
