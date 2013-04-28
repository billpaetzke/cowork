from django.db import models

class Space(models.Model):

    name = models.CharField(
            max_length=63,
            )
    address = models.CharField(
            max_length=255,
            )
    phone = models.CharField(
            max_length=31,
            )
    url = models.CharField(
            max_length=255,
            )
    email = models.EmailField()

    def __str__(self):

        return self.name
