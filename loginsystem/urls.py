from django.urls import path
from . import views

urlpatterns = [
    path('register', views.registerasnewuser, name = 'register'),
    path('login', views.loginuser, name = 'login'),
    path('registersave', views.registersave, name = 'registersave'),
    path('logincred', views.loginuserget, name = 'logincred'),
    path('password_reset_email', views.password_reset_email, name='password_reset_email'),
    path('password_reset_email_verification', views.password_reset_email_verification, name='password_reset_email_verification'),
    path('password_reset_view', views.password_reset_view, name='password_reset_view'),
    path('password_reset_done', views.password_reset_done, name='password_reset_done'),
    path('logout', views.logout, name = 'logout'),
]