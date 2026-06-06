from django.urls import path

from . import views

app_name = 'barbearia'

urlpatterns = [
    path('', views.home, name='home'),
    
    # Agendamentos
    path('agendamento/agendar/', views.agendar, name='agendar'),
    path('agendamento/<int:agendamento_id>/', views.agendamento_detail,name='agendamento_detail'), 
    path('agendamento/<int:agendamento_id>/update/', views.agendamento_update, name='update'),
    path('agendamento/<int:agendamento_id>/delete/', views.agendamento_delete, name='delete'),
    
    # User
    path('user/login/', views.login, name='login'),
    path('user/logout/', views.logout, name='logout'),
    path('user/register/', views.register, name='register'),
    ]