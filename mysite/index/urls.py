from django.urls import path
from .views import LoginView

app_name = 'index'

urlpatterns = [path('login/',LoginView.as_view()),]