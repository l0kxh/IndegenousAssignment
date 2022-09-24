from statistics import mode
from tkinter import TRUE
from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.TextField(max_length=200)
    description = models.TextField(null=True)

    def __str__(self) -> str:
        return self.description