from django import forms
from .models import quarto

input_estilo = {
    'style': 'width: 100%; padding: 10px; margin-bottom: 15px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box;'
}

class FormNome(forms.Form):
    nome = forms.CharField(label='Nome', max_length=20, widget=forms.TextInput(attrs=input_estilo))
    sobrenome = forms.CharField(label='Sobrenome', max_length=20, widget=forms.TextInput(attrs=input_estilo))
    email = forms.CharField(label='Email', max_length=50, widget=forms.EmailInput(attrs=input_estilo))
    idade = forms.CharField(label='Idade', max_length=3, widget=forms.TextInput(attrs=input_estilo))
    endereco = forms.CharField(label='Endereço', max_length=50, widget=forms.TextInput(attrs=input_estilo))

    QUARTOS_CHOICES = [(q.tipo, q.get_tipo_display()) for q in quarto.objects.all()]
    quarto = forms.ChoiceField(label='Quarto', choices=QUARTOS_CHOICES, widget=forms.Select(attrs=input_estilo))
    
    data = forms.DateField(label='Data', widget=forms.DateInput(attrs={'type': 'date', **input_estilo}))


class FormCadastro(forms.Form):
    first_name = forms.CharField(label="Nome", max_length=20, widget=forms.TextInput(attrs=input_estilo))
    last_name = forms.CharField(label="Sobrenome", max_length=20, widget=forms.TextInput(attrs=input_estilo))
    user = forms.CharField(label="Usuário", max_length=20, widget=forms.TextInput(attrs=input_estilo))
    email = forms.EmailField(label="Email", max_length=100, widget=forms.EmailInput(attrs=input_estilo))
    password = forms.CharField(label="Senha", widget=forms.PasswordInput(attrs=input_estilo))


class FormLogin(forms.Form):
    user = forms.CharField(label="Usuário", max_length=20, widget=forms.TextInput(attrs=input_estilo))
    password = forms.CharField(label="Senha", widget=forms.PasswordInput(attrs=input_estilo))
