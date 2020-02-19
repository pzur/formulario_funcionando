from django.shortcuts import render
from .models import Cliente
from .forms import ClienteForm



def Register_Cliente(request):
    if request.method=="POST":
        form=ClienteForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=ClienteForm()
    return render(request,'formulario.html',{'form':form})

# Create your views here.
