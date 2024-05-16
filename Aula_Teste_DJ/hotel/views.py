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
            var_email = form.cleaned_data['email']

            print(var_nome, var_email)

            return HttpResponse("<h1>Thanks</h1>")
    else:
        form = FormNome()

        return render(request, "nome.html", {"form": form})