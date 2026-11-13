from django.db import models
from .autor import Autor
from .categoria import Categoria


class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    autor_ficha = models.ForeignKey(
        Autor,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='libros',
        verbose_name='autor registrado',
    )
    fecha_publicacion = models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    isbn = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo
    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"
        ordering = ['titulo']