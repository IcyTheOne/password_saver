"""password_saver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.urls import views as auth_views
from users import views as user_views
from two_factor.urls import urlpatterns as tfurls
from two_factor.views import LoginView
from two_factor.views import SetupView
from two_factor.views import DisableView





urlpatterns = [
    path('admin/', admin.site.urls),
    #users app urls
#    path('users/', include('users.urls', namespace='users')),
    path(
        'two_factor/setup/',
        SetupView.as_view(),
        name='setup',
    ),
    path(
        'two_factor/disable/',
        DisableView.as_view(),
        name='disable',
    ),
    path(
        'login/',
        LoginView.as_view(template_name='two_factor/core/login.html'),
        name='login',
    ),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', user_views.register, name='register'),
    path('', include(tfurls)),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='users/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'
         ),
         name='password_reset_complete'),


    #vault app urls
    path('', include('vault.urls')),
]
