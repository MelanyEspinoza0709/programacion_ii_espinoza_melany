from django.urls import path
from catalogo.views.catalogo_views import categoria_create, categoria_list

urlpatterns = [
    path('categorias/', categoria_list, name='categoria_list'),
    path('categorias/crear/', categoria_create, name='categoria_create'),
]
