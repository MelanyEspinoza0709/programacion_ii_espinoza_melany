from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

from catalogo.models import Libro


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = [
            'titulo',
            'autor_ficha',
            'fecha_publicacion',
            'categoria',
            'isbn',
        ]
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'autor_ficha': forms.Select(attrs={'class': 'form-control'}),
            'fecha_publicacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control'}),
        }
        help_texts = {
            'autor_ficha': 'Selecciona la ficha del autor del libro.',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._autor_ficha_original = self.instance.autor_ficha_id
        if self.instance.pk and self._autor_ficha_original is None:
            self.fields['autor_ficha'].required = False

    def save(self, commit=True):
        libro = super().save(commit=False)
        autor = self.cleaned_data.get('autor_ficha')
        if autor and (
            not self.instance.pk or self._autor_ficha_original != autor.pk
        ):
            libro.autor = ' '.join(
                parte for parte in (autor.nombre, autor.apellido) if parte
            )

        if commit:
            libro.save()
            self.save_m2m()
        return libro

    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo')
        if titulo:
            titulo = titulo.strip()
            if not titulo:
                raise ValidationError('El título no puede estar vacío.')
        return titulo

    def clean_fecha_publicacion(self):
        fecha_publicacion = self.cleaned_data.get('fecha_publicacion')
        if fecha_publicacion and fecha_publicacion > timezone.localdate():
            raise ValidationError('La fecha de publicación no puede ser futura.')
        return fecha_publicacion

    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn')
        if self.instance.pk and isbn == self.instance.isbn:
            return isbn
        if not isbn or len(isbn) != 13 or not isbn.isascii() or not isbn.isdigit():
            raise ValidationError('El ISBN debe tener 13 dígitos y ser numérico.')
        return isbn