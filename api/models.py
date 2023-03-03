from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    # model Game for site
    name = models.CharField(max_length=255, db_index=True)
    platform = models.CharField(max_length=20)
    year = models.SmallIntegerField(default=1970)
    genre = models.CharField(max_length=127)
    global_sales = models.FloatField()

    def __str__(self):
        return self.name