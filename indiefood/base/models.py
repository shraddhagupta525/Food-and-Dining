from django.db import models

# Create your models here.

class orders(models.Model):
    email=models.CharField(max_length=20)
    phone_number=models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    Time=models.DateTimeField(auto_now_add=True)
    items=models.CharField(max_length=20)
    status=models.CharField(max_length=20, default="in progress")

    def __str__(self):
        return self.name

class tables(models.Model):
    name=models.CharField(max_length=20)
    phone_number=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    noofperson=models.CharField(max_length=5)
    tableType=models.CharField(max_length=20)
    Time=models.DateTimeField(max_length=50)

    def __str__(self):
        return self.name