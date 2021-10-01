from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    number = models.PositiveIntegerField()
    message = models.TextField()

    def __str__(self) -> str:
        return self.name