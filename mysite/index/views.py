from django.views.generic import FormView
from django.contrib.auth.forms import AuthenticationForm

class SignUpView(FormView):
    form_class = AuthenticationForm
    template_name = 'signUp.html'

class LogInView(FormView):
    form_class = AuthenticationForm
    template_name = 'logIn.html'
