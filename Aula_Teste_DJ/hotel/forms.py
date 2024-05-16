from django import forms

class FormNome(forms.Form):
    nome = forms.CharField(label='Nome', max_length=20)
    email = forms.CharField(label='Email', max_length=50)