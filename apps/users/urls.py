from django.urls import re_path
from rest_auth.registration.views import RegisterView
from rest_auth.views import (
    LoginView, LogoutView, PasswordChangeView
)

app_name = "users"

urlpatterns = [

    # Here are some of the most necessary endpoints to provide registration/login
    re_path(r'^login/$', LoginView.as_view(), name='rest_login'),
    re_path(r'^logout/$', LogoutView.as_view(), name='rest_logout'),
    re_path(r'^password/change/$', PasswordChangeView.as_view(), name='rest_password_change'),
    re_path(r'^registration/$', RegisterView.as_view(), name='rest_register'),
]
