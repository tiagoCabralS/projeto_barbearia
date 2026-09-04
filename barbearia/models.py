from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import timedelta

# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    name = models.CharField(max_length=50)
    duracao = models.DurationField(default=timedelta(minutes=30))

    def __str__(self):
        return self.name

class Perfil(models.Model):
    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='perfil',
    )
    telefone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.usuario.username

class Agendamento(models.Model):
    date = models.DateField() 
    horario = models.TimeField()
    fim = models.TimeField(null=True)
    category = models.ForeignKey(
        Category, 
        blank=True,
        on_delete=models.SET_NULL, null=True
        )
    cliente = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True, null=True
    )