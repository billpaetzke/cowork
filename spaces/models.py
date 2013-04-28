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
            blank=True,
            )
    url = models.CharField(
            max_length=255,
            blank=True,
            )
    email = models.EmailField(
            max_length=255,
            blank=True,
            )

    def __str__(self):

        return self.name

# Note: I looked into inheritance (e.g. PendingSpace inherits Space)
#       but it seemed too complex to handle in ORM at this point
#       KISS!!
class PendingSpace(models.Model):
    """To be used for anonymous users to add new spaces--requiring approval"""
    
    name = models.CharField(
            max_length=63,
            )
    address = models.CharField(
            max_length=255,
            )

    def __str__(self):

        return ' '.join([self.name, "--", self.address])
