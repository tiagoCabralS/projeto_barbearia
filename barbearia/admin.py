from django.contrib import admin
from barbearia import models

# Register your models here.
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(models.Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('date', 'category')

@admin.register(models.Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'telefone')