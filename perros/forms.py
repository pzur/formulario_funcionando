from django.forms import ModelForm
from django import forms
from .models import Cliente, Mascota,Paseador

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = '__all__'


class MascotaForm(forms.ModelForm):

    class Meta:
        model = Mascota
        fields = '__all__'


class PaseadorForm(forms.ModelForm):

    class Meta:
        model = Paseador
        fields = '__all__'