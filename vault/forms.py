from django import forms
from .models import SavedAccount
#for password encryption:
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class VaultAccountForm(forms.ModelForm):

    class Meta:
        model = SavedAccount
        fields = ('websiteName', 'websiteUrl', 'emailSpecial', 'usernameSpecial', 'passwordSpecial')
        labels = {
            'websiteName': ('Website name '),
            'websiteUrl': ('Website Url '),
            'emailSpecial': ('Account email '),
            'usernameSpecial': ('Account username '),
            'passwordSpecial': ('Account password ')
        }
        # # make password in dots when entering in the password field on the cards
        # widgets = {
        #     'passwordSpecial': forms.PasswordInput(), #this is used to make it in dots(but )
        # }
        help_texts = {
            'websiteName': ('Some useful help text.'),
        }
        error_messages = {
            'websiteName': {
                'max_length': ("This writer's name is too long."),
            },
        }
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