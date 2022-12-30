from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Tarea
import time
# Create your views here.
def nn(request):
	return redirect("home")

def home(request):
	base = Tarea.objects.all()
	dic = {"lista":base}

	return render(request,"index.html", dic)

def registrar(request):
	fechaa = time.strftime("%d/%m/20%y %I:%M")
	nombree = request.POST["nombrex"]
	descripcione = request.POST["descripcionx"]
	if nombree=="":
		return redirect("home")

	else:
		agragar = Tarea.objects.create(nombre = nombree, fecha= fechaa, descripcion = descripcione)

	return HttpResponseRedirect("home")

def edicion(request,nombr):
	base = Tarea.objects.get(nombre=nombr)
	des=base.descripcion
	dic ={"nom":nombr,"des":des}
	return render(request,"editar.html",dic)

def editar(request):
	fechaa = time.strftime("%d/%m/20%y %I:%M")
	nombree = request.POST["nombrex"]
	descripcione = request.POST["descripcionx"]

	bo = Tarea.objects.get(nombre=nombree)
	bo.nombre=nombree
	bo.descripcion=descripcione
	bo.fecha=fechaa
	bo.save()
	return redirect("home")


def borrar(request,nombre):
	bo = Tarea.objects.get(nombre=nombre)
	bo.delete()
	return redirect("home")

def ver(request,nom):
	base = Tarea.objects.get(nombre=nom)
	des=base.descripcion
	dic ={"nom":nom,"des":des}
	return render(request,"ver.html",dic)