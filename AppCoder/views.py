from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import Viajero, Destino, Establecimiento
from AppCoder.forms import ViajeroFormulario, DestinoFormulario, EstablecimientoFormulario

# Create your views here.

def inicio(request):

      return render(request, "AppCoder/inicio.html")

def viajeros(request):

      if request.method == 'POST':

            miFormulario = ViajeroFormulario(request.POST)

            print(miFormulario)

            if miFormulario.is_valid:

                  informacion = miFormulario.cleaned_data

                  viajero = Viajero (nombre=informacion['nombre'], apellido=informacion['apellido'],
                  email=informacion['email'], profesion=informacion['profesion']) 

                  viajero.save()

                  return render(request, "AppCoder/inicio.html")

      else: 

            miFormulario= ViajeroFormulario()

      return render(request, "AppCoder/viajeros.html", {"miFormulario":miFormulario})

def destinos(request):

      if request.method == 'POST':

            miFormulario = DestinoFormulario(request.POST)

            print(miFormulario)

            if miFormulario.is_valid:

                  informacion = miFormulario.cleaned_data

                  destino = Destino (nombre=informacion['nombre'], pais=informacion['pais']) 

                  destino.save()

                  return render(request, "AppCoder/inicio.html")

      else: 

            miFormulario= DestinoFormulario()

      return render(request, "AppCoder/destinos.html", {"miFormulario":miFormulario})

def establecimientos(request):

      if request.method == 'POST':

            miFormulario = EstablecimientoFormulario(request.POST)

            print(miFormulario)

            if miFormulario.is_valid:

                  informacion = miFormulario.cleaned_data

                  establecimiento = Establecimiento (nombre=informacion['nombre'], rubro=informacion['rubro'],calificacion=informacion['calificacion']) 

                  establecimiento.save()

                  return render(request, "AppCoder/inicio.html")

      else: 

            miFormulario= EstablecimientoFormulario()

      return render(request, "AppCoder/establecimientos.html", {"miFormulario":miFormulario})

def buscar(request):

      if  request.GET["nombre"]:

            nombre = request.GET['nombre'] 
            destino = Destino.objects.filter(nombre__icontains=nombre)

            return render(request, "AppCoder/inicio.html", {"nombre":nombre, "destino":destino})

      else: 

	      respuesta = "No enviaste datos"

      return HttpResponse(respuesta)