from django.shortcuts import render
from .models import Cliente
from .forms import ClienteForm, MascotaForm, PaseadorForm



def Register_Cliente(request):
    if request.method=="POST":
        form=ClienteForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=ClienteForm()
    return render(request,'formulario.html',{'form':form})


def Register_Mascota(request):
    if request.method=="POST":
        form=MascotaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=MascotaForm()
    return render(request,'formulario_mascota.html',{'form':form})


def Register_Paseador(request):
    if request.method=="POST":
        form=PaseadorForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=PaseadorForm()
    return render(request,'formulario_paseador.html',{'form':form})


# Create your views here.
