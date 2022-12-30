from django.urls import path
from . import views

urlpatterns = [
   path("home",views.home, name = "home"),
   path("",views.nn, name = ""),
   path("registrar",views.registrar, name = "registrar"),
   path("editar/<nombr>",views.edicion, name = "edicion"),
   path("borrar/<nombre>",views.borrar, name = "borrar"),
   path("ver/<nom>",views.ver, name = "ver"),
   path("editar",views.editar, name = "editar"),



]