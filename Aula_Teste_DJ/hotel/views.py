from django.shortcuts import render, HttpResponse
from .models import *
from .forms import FormNome

# Create your views here.

def homepage(request):
    # return HttpResponse("<h1> Hello World </h1>")
    context = {}
    dados_hotel = hotel.objects.all()
    context["dados_hotel"] = dados_hotel    
    return render(request,'homepage.html' , context)

def quartos(request):
    context = {}
    context2 = {}
    dados_quarto = quarto.objects.all() 
    dados_hotel = hotel.objects.all()
    
    context["dados_quarto"] = dados_quarto
    
    return render(request, 'quartos.html', context)

def nome(request):
    if request.method == "POST":
        form = FormNome(request.POST)
        if form.is_valid():

            var_nome = form.cleaned_data['nome']
            var_sobrenome = form.cleaned_data['sobrenome']
            var_email = form.cleaned_data['email']
            var_idade = form.cleaned_data['idade']
            var_endereco = form.cleaned_data['endereco']
            var_quarto = form.cleaned_data['quarto']
            var_data = form.cleaned_data['data']

            user = usuario(nome=var_nome, sobrenome=var_sobrenome, email=var_email, idade=var_idade, endereco=var_endereco, quarto=var_quarto, data=var_data)
            user.save()

            return HttpResponse("<div style=\"font-family: 'Courier New', Courier, monospace; background-color: #f5c2dac6; text-align: center; padding: 20px; border-radius: 8px; margin: 45px;\"><h1>Reserva Realizada com Sucesso!</h1><br><h1>Obrigado Pela Preferência!</h1></div>")

    else:
        form = FormNome()

        return render(request, "reserva.html", {"form": form})