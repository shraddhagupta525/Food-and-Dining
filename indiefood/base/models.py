from django.db import models


# Create your models here.

class orders(models.Model):
    email=models.CharField(max_length=20)
    phone_number=models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    Time=models.DateTimeField(auto_now_add=True)
    items=models.CharField(max_length=20)

    def __str__(self):
        return self.name