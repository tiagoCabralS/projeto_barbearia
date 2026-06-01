from django.db import models
from django.utils import timezone


# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Agendamento(models.Model):
    date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(
        Category, 
        blank=True,
        on_delete=models.SET_NULL, null=True
        )