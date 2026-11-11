
from django.contrib.auth.views import LoginView, LogoutView


class BibliotecaLoginView(LoginView):
    template_name = 'catalogo/authentication/login.html'
    redirect_authenticated_user = True

class BibliotecaLogoutView(LogoutView):
    template_name = 'catalogo/authentication/logout.html'
    next_page = 'login'