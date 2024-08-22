from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Cliente, Carro, Renta
from .forms import ClienteForm, CarroForm, RentaForm, BuscarForm

def inicio(request):
    return render(request, 'management/inicio.html')

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = ClienteForm()
    return render(request, 'management/agregar_cliente.html', {'form': form})

def agregar_carro(request):
    if request.method == 'POST':
        form = CarroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = CarroForm()
    return render(request, 'management/agregar_carro.html', {'form': form})

def agregar_renta(request):
    if request.method == 'POST':
        form = RentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = RentaForm()
    return render(request, 'management/agregar_renta.html', {'form': form})

def buscar(request):
    if request.method == 'POST':
        form = BuscarForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            clientes = Cliente.objects.filter(nombre__icontains=query)
            carros = Carro.objects.filter(marca__icontains=query)
            rentas = Renta.objects.filter(cliente__nombre__icontains=query)
            return render(request, 'management/resultados_busqueda.html', {
                'clientes': clientes,
                'carros': carros,
                'rentas': rentas
            })
    else:
        form = BuscarForm()
    return render(request, 'management/buscar.html', {'form': form})
