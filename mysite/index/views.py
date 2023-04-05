from django.views.generic import FormView
from django.contrib.auth.forms import AuthenticationForm

class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'logInPage.html'
