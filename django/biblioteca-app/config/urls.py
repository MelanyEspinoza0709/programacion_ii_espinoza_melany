from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path


def redirect_to_catalogo(request):
    return redirect('categoria_list')


urlpatterns = [
    path('', redirect_to_catalogo),
    path('admin/', admin.site.urls),
    path('catalogo/', include('catalogo.urls.categoria_urls')),
]
