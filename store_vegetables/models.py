from django.db import models


class Vegetable(models.Model):
    title = models.CharField(max_length=150)
    price = models.IntegerField()

    def __str__(self):
        return self.title
