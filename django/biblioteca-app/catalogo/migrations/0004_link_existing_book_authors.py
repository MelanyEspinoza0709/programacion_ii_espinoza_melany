from django.db import migrations


def link_existing_book_authors(apps, schema_editor):
    Autor = apps.get_model('catalogo', 'Autor')
    Libro = apps.get_model('catalogo', 'Libro')
    database = schema_editor.connection.alias

    for libro in Libro.objects.using(database).filter(autor_ficha__isnull=True).iterator():
        nombre_completo = (libro.autor or '').strip()
        if not nombre_completo:
            continue

        partes = nombre_completo.rsplit(maxsplit=1)
        if len(partes) == 2:
            nombre, apellido = partes
        else:
            nombre, apellido = partes[0], ''

        autor, _ = Autor.objects.using(database).get_or_create(
            nombre=nombre,
            apellido=apellido,
        )
        Libro.objects.using(database).filter(pk=libro.pk).update(
            autor_ficha_id=autor.pk,
        )


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0003_autor_and_libro_autor_ficha'),
    ]

    operations = [
        migrations.RunPython(
            link_existing_book_authors,
            migrations.RunPython.noop,
        ),
    ]
