from django.db import models

class FibonacciNumber(models.Model):
    value = models.BigIntegerField()

    def __str__(self):
        return str(self.value)
