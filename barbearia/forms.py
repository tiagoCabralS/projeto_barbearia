from django import forms
from barbearia.models import Agendamento
from django.utils import timezone
from django.core.exceptions import ValidationError

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = (
            'date', 'category',
        )
    
    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        
        if date and date <= timezone.now():
            self.add_error('date', ValidationError('A data e hora do agendamento devem ser no futuro.', code='invalid'))
        if date and Agendamento.objects.filter(date=date).exists():
            self.add_error('date', ValidationError('Já existe um agendamento para esta data e hora.', code='invalid'))
        
        return cleaned_data