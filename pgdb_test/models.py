from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=240)
    email = models.EmailField(unique=True)
    created = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.name