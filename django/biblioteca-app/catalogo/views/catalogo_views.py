from django.contrib import messages
from django.shortcuts import redirect, render

from catalogo.models import Categoria
from forms.categoria_form import CategoriaForm


def categoria_list(request):
    categorias = Categoria.objects.all()
    return render(
        request,
        'catalogo/categorias/categorias_list.html',
        {'categorias': categorias},
    )


def categoria_create(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría creada correctamente.')
            return redirect('categoria_list')
    else:
        form = CategoriaForm()

    return render(
        request,
        'catalogo/categorias/formulario.html',
        {'form': form},
    )