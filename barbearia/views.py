from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from barbearia.models import Agendamento
from barbearia.forms import AgendamentoForm
from django.utils import timezone
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from barbearia.forms import UserRegistrationForm

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

@login_required(login_url='barbearia:login')
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
    
@login_required(login_url='barbearia:login')
def agendamento_update(request, agendamento_id):
    agendamento = get_object_or_404(
        Agendamento,
        id=agendamento_id
    )
    
    from_action = reverse('barbearia:update', args=[agendamento_id])
    
    if request.method == 'POST':
        form = AgendamentoForm(request.POST, instance=agendamento)
        
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
        'form': AgendamentoForm(instance=agendamento),
        'site_title': f'Atualizar Agendamento {agendamento_id} - ',
    }
    
    return render(
        request, 
        'barbearia/agendar.html',
        context
        )

@login_required(login_url='barbearia:login')
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
 
@login_required(login_url='barbearia:login')   
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
    
def register(request):
    form = UserRegistrationForm()
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro realizado com sucesso! Agora você pode fazer login.')
            return redirect('barbearia:login')
        messages.error(request, 'Registro falhou. Verifique os erros e tente novamente.')
    
    return render(
        request,
        'barbearia/register.html',
        {
            'site_title': 'Register - ',
            'form': form
        }
    )
    
def login(request):
    form = AuthenticationForm(request)
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Login realizado com sucesso!')
            return redirect('barbearia:home')
        messages.error(request, 'Login falhou. Verifique suas credenciais e tente novamente.')
        
    
    return render(
        request,
        'barbearia/login.html',
        {
            'site_title': 'Login - ',
            'form': form
        }
    )

@login_required(login_url='barbearia:login')    
def logout(request):
    auth.logout(request)
    messages.info(request, 'Logout realizado com sucesso!')
    return redirect('barbearia:login')