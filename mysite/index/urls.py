from django.urls import path
from .views import SignUpView, LogInView

app_name = 'index'

urlpatterns = [path('sign-up/',SignUpView.as_view(),name='sign_up'),
               path('log-in/',LogInView.as_view(),name='log_in')]