from django.urls import path

from . import views

app_name = 'barbearia'

urlpatterns = [
    path('', views.home, name='home'),
    path('agendar/', views.agendar, name='agendar'),
    path('agendamento/<int:agendamento_id>/', views.agendamento_detail,name='agendamento_detail'), 
    path('agendamento/<int:agendamento_id>/delete/', views.agendamento_delete, name='delete'),
]