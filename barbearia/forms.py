from django import forms
from barbearia.models import Agendamento
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime, timedelta

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = (
            'date', 'horario', 'category', 
        )
        
        widgets = {
            'date': forms.DateInput(
                attrs={'class': 'formulario-campo', 'type': 'date', 'placeholder': 'Data do agendamento'}
                ),
            'category': forms.Select(
                attrs = {'class': 'formulario-campo', 'type': 'select'}
            ),
            'horario': forms.TimeInput(
                attrs = {'class': 'formulario-campo', 'type': 'time', 'placeholder': 'Horário do agendamento'}
            )
        }
    
    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        horario = cleaned_data.get('horario')
        data_fake = datetime.combine(datetime.today(), horario)
        fim = (data_fake + timedelta(hours=1)).time()
        
        print(horario, fim)
        
        if date and date < timezone.now().date():
            self.add_error('date', ValidationError('A data e hora do agendamento devem ser no futuro.', code='invalid'))
        if date and Agendamento.objects.filter(date=date).exists() and Agendamento.objects.filter(horario=horario).exists():
            self.add_error('date', ValidationError('Já existe um agendamento para esta data e hora.', code='invalid'))
        # Checar se o horário está sobrepondo os horários de algum agendamento já existente
        if Agendamento.objects.filter(date=date):
            agendamentos = Agendamento.objects.filter(date=date)
            print(agendamentos)
            for agendamento in agendamentos:
                print(agendamento.horario)
                if agendamento.horario <= horario and agendamento.fim >= horario:
                    self.add_error('date', ValidationError('Horário indisponível, pois sobrepõe outro agendamento.', code='invalid'))
                if agendamento.horario <= fim and agendamento.fim >= fim:
                    self.add_error('date', ValidationError('Horário indisponível, pois sobrepõe outro agendamento.', code='invalid'))
        
        return cleaned_data

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30, 
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'formulario-campo', 'placeholder': 'Nome'}
            )
        )
    last_name = forms.CharField(
        max_length=150, 
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'formulario-campo', 'placeholder': 'Sobrenome'}
            )
        )
    username = forms.CharField(
        max_length=150, 
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'formulario-campo', 'placeholder': 'Username'}
            )
        )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={'class': 'formulario-campo', 'placeholder': 'Email'}
            )
        )
    password1 = forms.CharField(
        label='Password', 
        widget=forms.PasswordInput(
            attrs={'class': 'formulario-campo', 'placeholder': 'Senha'}), 
        required=True
        )
    password2 = forms.CharField(
        label='Confirm Password', 
        widget=forms.PasswordInput(
            attrs={'class': 'formulario-campo', 'placeholder': 'Confirme a senha'}), 
        required=True
        )
    
    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'username', 'email', 'password1', 'password2',
        ]
        
        widgets = {
            'last_name': forms.TextInput(
                attrs={'class': 'formulario-campo', 'type': 'text', 'placeholder': 'Sobrenome'}
            ),
            'username': forms.TextInput(
                attrs={'class': 'formulario-campo', 'type': 'text', 'placeholder': 'Username'}
            ),
            'email': forms.EmailInput(
                attrs={'class': 'formulario-campo', 'type': 'email', 'placeholder': 'Email'}
            ),
            'password1': forms.PasswordInput(
                attrs={'class': 'formulario-campo', 'type': 'password', 'placeholder': 'Senha'}
            ),
            'password2': forms.PasswordInput(
                attrs={'class': 'formulario-campo', 'type': 'password', 'placeholder': 'Repita a senha'}
            )
        }            
            
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        
        if password1 and password2 and password1 != password2:
            self.add_error('password2', ValidationError('As senhas não coincidem.', code='invalid'))
        
        return cleaned_data