from django.db import models


class Schema(models.Model):
    route = models.CharField(max_length=50, required=True)
    name = models.CharField(max_length=50, required=True)

    def __str__(self):
        return self.name

