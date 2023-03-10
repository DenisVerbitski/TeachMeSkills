from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


app_name = 'user'
urlpatterns = [
    path('login_user', views.login_user, name='login'),
    path('logout_user', views.logout_user, name='logout'),
    path('register_user', views.register_user, name='register_user'),
    path('change_pass/', views.CustomPasswordChangeView.as_view(), name='password_change'),
    path('password_success', auth_views.PasswordResetDoneView.as_view(
                        template_name = 'authenticate/password_success.html'
                    ), name='password_success'),
]   