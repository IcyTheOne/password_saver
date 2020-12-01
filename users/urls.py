from django.conf.urls import url
from django.contrib.auth.views import LoginView
from . import views
app_name = 'password_saver'
urlpatterns = [
 # Login page
    url('login/' , LoginView.as_view(template_name='login.html'))
]