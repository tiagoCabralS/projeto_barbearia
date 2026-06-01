from django.shortcuts import render
from barbearia.models import Agendamento

# Create your views here.

def home(request):
    agendamentos = Agendamento.objects.all().order_by('date')
    
    context = {
        'site_title': 'Home - ',
        'agendamentos': agendamentos,
    }
    
    return render(
        request, 
        'barbearia/index.html',
        context
        )

def agendar(request):
    context = {
        'site_title': 'Agendar - ',
    }
    
    return render(
        request, 
        'barbearia/agendar.html',
        context
        )

def agendamento_detail(request, agendamento_id):
    agendamento = Agendamento.objects.get(id=agendamento_id)
    
    context = {
        'site_title': f'Agendamento {agendamento_id} - ',
        'agendamento': agendamento,
    }
    
    return render(
        request, 
        'barbearia/agendamento_detail.html',
        context
        )