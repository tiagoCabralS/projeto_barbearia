from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from barbearia.models import Agendamento
from barbearia.forms import AgendamentoForm
from django.utils import timezone

# Create your views here.

def home(request):
    agendamentos_prox = Agendamento\
        .objects\
        .filter(date__gte=timezone.now())\
        .order_by('date')
    
    agendamentos_pass = Agendamento\
        .objects\
        .filter(date__lt=timezone.now())\
        .order_by('date')
    
    context = {
        'site_title': 'Home - ',
        'agendamentos': [agendamentos_prox, agendamentos_pass],
    }
    
    return render(
        request, 
        'barbearia/index.html',
        context
        )

def agendar(request):
    from_action = reverse('barbearia:agendar')
    
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        
        context = {
            'from_action': from_action,
            'form': form,
        }
        if form.is_valid():
            form.save()
            return redirect('barbearia:home')
        
        return render(
            request, 
            'barbearia/agendar.html',
            context
        )
    
    context = {
        'form': AgendamentoForm(),
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
    
def agendamento_delete(request, agendamento_id):
    agendamento = get_object_or_404(
        Agendamento,
        id=agendamento_id
    )
    
    confirmation = request.POST.get('confirmation', 'no')
    print('Confirmation: ', confirmation)
    
    if confirmation == 'yes':
        agendamento.delete()
        return redirect('barbearia:home')
    
    return render(
        request,
        'barbearia/agendamento_detail.html',
        {
            'site_title': f'Excluir Agendamento {agendamento_id} - ',
            'agendamento': agendamento,
            'confirmation': confirmation,
        }
    )