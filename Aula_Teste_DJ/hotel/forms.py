from django import forms
from .models import quarto

class FormNome(forms.Form):
    nome = forms.CharField(label='Nome', max_length=20)
    sobrenome = forms.CharField(label='Sobrenome', max_length=20)
    email = forms.CharField(label='Email', max_length=50)
    idade = forms.CharField(label='Idade', max_length=3)
    endereco = forms.CharField(label='Endereço', max_length=50)

    QUARTOS_CHOICES = [(q.tipo, q.get_tipo_display()) for q in quarto.objects.all()]
    quarto = forms.ChoiceField(label='Quarto', choices=QUARTOS_CHOICES)
    
    data = forms.CharField(label='Data', max_length=20)