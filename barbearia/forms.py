from django import forms
from barbearia.models import Agendamento
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = (
            'date', 'category',
        )
        
        widgets = {
            'date': forms.DateTimeInput(
                attrs={'class': 'formulario-campo', 'type': 'datetime-local', 'placeholder': 'Data e hora do agendamento'}
                ),
            'category': forms.Select(
                attrs = {'class': 'formulario-campo', 'type': 'select'}
            )
        }
    
    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        
        if date and date <= timezone.now():
            self.add_error('date', ValidationError('A data e hora do agendamento devem ser no futuro.', code='invalid'))
        if date and Agendamento.objects.filter(date=date).exists():
            self.add_error('date', ValidationError('Já existe um agendamento para esta data e hora.', code='invalid'))
        
        return cleaned_data

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=150, required=True)
    username = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput, required=True)
    
    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'username', 'email', 'password1', 'password2',
        ]
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        
        if password1 and password2 and password1 != password2:
            self.add_error('password2', ValidationError('As senhas não coincidem.', code='invalid'))
        
        return cleaned_data