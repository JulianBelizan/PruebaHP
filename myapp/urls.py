# MyApp/urls.py
from django.urls import path
from .views import lista_pokemon,filtro_peso,filtro_grass,filtro_flying,filtro_contrario

urlpatterns = [
    path('', lista_pokemon, name="Proyecto Pokemon"),
    path('filtro1/', filtro_peso),
    path('filtro2/', filtro_grass),
    path('filtro3/', filtro_flying),
    path('filtro4/', filtro_contrario),
]
