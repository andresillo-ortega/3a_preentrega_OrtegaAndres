from django import forms
from .models import Cliente, Carro, Renta

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class CarroForm(forms.ModelForm):
    class Meta:
        model = Carro
        fields = '__all__'

class RentaForm(forms.ModelForm):
    class Meta:
        model = Renta
        fields = '__all__'

class BuscarForm(forms.Form):
    query = forms.CharField(label='Buscar', max_length=100)
