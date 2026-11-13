from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import ProtectedError
from django.shortcuts import get_object_or_404, redirect, render

from catalogo.models import Autor
from forms.autor_form import AutorForm


@login_required
@permission_required('catalogo.view_autor', raise_exception=True)
def autor_list(request):
    autores = Autor.objects.all()
    return render(request, 'catalogo/autores/autor_list.html', {'autores': autores})


@login_required
@permission_required('catalogo.add_autor', raise_exception=True)
def autor_create(request):
    if request.method == 'POST':
        formulario = AutorForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Autor creado correctamente.')
            return redirect('autor_list')
    else:
        formulario = AutorForm()

    return render(request, 'catalogo/autores/formulario.html', {'formulario': formulario})


@login_required
@permission_required('catalogo.change_autor', raise_exception=True)
def autor_update(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        formulario = AutorForm(request.POST, instance=autor)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Autor actualizado correctamente.')
            return redirect('autor_list')
    else:
        formulario = AutorForm(instance=autor)

    return render(request, 'catalogo/autores/formulario.html', {'formulario': formulario})


@login_required
@permission_required('catalogo.delete_autor', raise_exception=True)
def autor_delete(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        try:
            autor.delete()
        except ProtectedError:
            messages.error(request, 'No se puede eliminar el autor porque tiene libros asociados.')
        else:
            messages.success(request, 'Autor eliminado correctamente.')
        return redirect('autor_list')

    return render(
        request,
        'catalogo/autores/confirm_delete.html',
        {'autor': autor},
    )
