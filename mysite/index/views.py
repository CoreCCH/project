from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import MyUserCreationForm
from .models import CustomUser
from django.views.generic import View, TemplateView
from django.contrib.auth.models import User


class SignUpView(TemplateView):
    template_name = 'signUp.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        '''Put the information you wants to pass into context.'''
        return context

    def dispatch(self, *args, **kwargs):
        if self.request.method == 'POST':
            __first_name = self.request.POST.get("first_name")
            __last_name = self.request.POST.get("last_name")
            __email = self.request.POST.get("email")
            __password = self.request.POST.get("password")
            if not CustomUser.objects.filter(email=__email).exists():
                __user = CustomUser.objects.create_user(email=__email, 
                                                    password=__password, 
                                                    first_name=__first_name,
                                                    last_name = __last_name)
                return redirect('index:log_in')
            else:
                context = {'error_message': 'Email already exists'}
                return render(self.request, self.template_name, context)
     
        else:
            return super().dispatch(*args, **kwargs)   

class LogInView(View):
    template_name = 'logIn.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    
    