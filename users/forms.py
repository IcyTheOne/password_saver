from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#for password encryption:
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        # #Basic code to generate key from a password:
        # #Will change ut by adding the email in the salting part too
        # password_provided = "password1"
        # password = str.encode(password_provided)    #converting to bytes (I HOPE)
        # salt = os.urandom(16)
        # kdf = PBKDF2HMAC(
        #     algorithm=hashes.SHA256(),
        #     length=32,
        #     salt=salt,
        #     iterations=100000,  #can increase this number ofc (go big or go home)
        #     backend=default_backend()
        # )
        # key = base64.urlsafe_b64decode(kdf.derive(password))