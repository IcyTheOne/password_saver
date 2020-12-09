from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'vault-home'),
    # path('', views.storeVaultAccount, name= 'vault-home'),
    # path('', views.storeVaultAccount, name='vault-new-account-form')
]