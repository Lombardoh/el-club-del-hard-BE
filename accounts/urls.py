from django.urls import path
from accounts.views import registration_view, login_view

from rest_framework.authtoken.views import obtain_auth_token

app_name = 'accounts'

urlpatterns = [
    path('register', registration_view, name='register'),
    path('login', login_view, name='login'),
]
