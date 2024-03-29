from django.urls import path
from accounts.views import registration_view, login_view, account_available, email_available, RequestPasswordResetEmail, PasswordTokenCheckAPI

from rest_framework.authtoken.views import obtain_auth_token

app_name = 'accounts'

urlpatterns = [
    path('register', registration_view, name='register'),
    path('login', login_view, name='login'),
    path('account_available/<str:username>', account_available, name='account_available'),
    path('email_available/<str:email>', email_available, name='email_available'),
    path('password-reset-email/', RequestPasswordResetEmail.as_view(), name='password-reset-email'),
    path('password-reset-confirm/<str:token>', PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
]
