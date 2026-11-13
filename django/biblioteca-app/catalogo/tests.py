from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from catalogo.models import Autor, Categoria, Libro
from forms.libro_form import LibroForm


class AutorFeatureTests(TestCase):
    def setUp(self):
        user = get_user_model().objects.create_superuser(
            username='bibliotecaria',
            email='bibliotecaria@example.com',
            password='test-password',
        )
        self.client.force_login(user)

    def test_author_crud_views_are_connected(self):
        response = self.client.get(reverse('autor_list'))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(
            reverse('autor_create'),
            {
                'nombre': 'Gabriel',
                'apellido': 'Garcia Marquez',
                'nacionalidad': 'Colombiana',
                'fecha_nacimiento': '1927-03-06',
            },
        )
        self.assertRedirects(response, reverse('autor_list'))
        autor = Autor.objects.get(nombre='Gabriel')

        self.assertEqual(
            self.client.get(reverse('autor_update', args=[autor.pk])).status_code,
            200,
        )
        self.assertEqual(
            self.client.get(reverse('autor_delete', args=[autor.pk])).status_code,
            200,
        )

        response = self.client.post(reverse('autor_delete', args=[autor.pk]))
        self.assertRedirects(response, reverse('autor_list'))
        self.assertFalse(Autor.objects.filter(pk=autor.pk).exists())

    def test_existing_book_author_text_is_preserved_with_author_link(self):
        categoria = Categoria.objects.create(nombre='Novela')
        autor = Autor.objects.create(nombre='Isabel', apellido='Allende')
        libro = Libro.objects.create(
            titulo='La casa de los espíritus',
            autor='Nombre previo tal como estaba',
            autor_ficha=autor,
            fecha_publicacion='1982-01-01',
            categoria=categoria,
            isbn='9789500727361',
        )

        libro.refresh_from_db()
        self.assertEqual(libro.autor, 'Nombre previo tal como estaba')
        self.assertEqual(libro.autor_ficha, autor)

    def test_book_form_links_author_and_searches_by_author_name(self):
        categoria = Categoria.objects.create(nombre='Ensayo')
        autor = Autor.objects.create(nombre='Rosa', apellido='Montero')
        self.assertEqual(
            self.client.get(reverse('create_libro')).status_code,
            200,
        )

        response = self.client.post(
            reverse('create_libro'),
            {
                'titulo': 'La ridícula idea de no volver a verte',
                'autor_ficha': autor.pk,
                'fecha_publicacion': '2013-01-01',
                'categoria': categoria.pk,
                'isbn': '9788432222814',
            },
        )
        self.assertRedirects(response, reverse('libro_list'))
        libro = Libro.objects.get(titulo='La ridícula idea de no volver a verte')
        self.assertEqual(libro.autor_ficha, autor)
        self.assertEqual(libro.autor, 'Rosa Montero')

        response = self.client.get(reverse('libro_list'), {'pista': 'Montero'})
        self.assertContains(response, 'La ridícula idea de no volver a verte')
        self.assertContains(response, 'Rosa Montero')

    def test_linked_author_cannot_be_deleted(self):
        categoria = Categoria.objects.create(nombre='Cuento')
        autor = Autor.objects.create(nombre='Jorge', apellido='Borges')
        Libro.objects.create(
            titulo='Ficciones',
            autor='Jorge Borges',
            autor_ficha=autor,
            fecha_publicacion='1944-01-01',
            categoria=categoria,
            isbn='9789500727362',
        )

        response = self.client.post(reverse('autor_delete', args=[autor.pk]))

        self.assertRedirects(response, reverse('autor_list'))
        self.assertTrue(Autor.objects.filter(pk=autor.pk).exists())


class LibroFormValidationTests(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(nombre='Historia')

    def test_new_book_requires_a_thirteen_digit_isbn(self):
        formulario = LibroForm(
            data={
                'titulo': 'Libro nuevo',
                'autor': 'Autora de prueba',
                'autor_ficha': '',
                'fecha_publicacion': '2020-01-01',
                'categoria': self.categoria.pk,
                'isbn': '12345',
            }
        )

        self.assertFalse(formulario.is_valid())
        self.assertIn('isbn', formulario.errors)

    def test_existing_isbn_can_be_kept_while_editing_a_book(self):
        libro = Libro.objects.create(
            titulo='Libro anterior',
            autor='Autor de prueba',
            fecha_publicacion='2020-01-01',
            categoria=self.categoria,
            isbn='ISBN legado',
        )
        formulario = LibroForm(
            data={
                'titulo': 'Libro actualizado',
                'autor': libro.autor,
                'autor_ficha': '',
                'fecha_publicacion': '2020-01-01',
                'categoria': self.categoria.pk,
                'isbn': libro.isbn,
            },
            instance=libro,
        )

        self.assertTrue(formulario.is_valid(), formulario.errors)
        formulario.save()
        libro.refresh_from_db()
        self.assertEqual(libro.isbn, 'ISBN legado')
        self.assertEqual(libro.titulo, 'Libro actualizado')
