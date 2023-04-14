from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'password')

class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'password')