from django.db import models


class Schema(models.Model):
    route = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class AppLayout(models.Model):
    pass
