from django.db import models
from django.contrib.auth.models import User
from fernet_fields import EncryptedTextField
from fernet_fields import EncryptedCharField


# Create your models here.

#the word special in the variables declaration specifies that those variables are for the username/password/etc.
#for the specific site they wanna add the credentials for (ex. Facebook, Gmail, etc.),
#for now the user creation for our site is at http://127.0.0.1:8000/admin/auth/user/

class SavedAccount(models.Model):
    websiteName = models.CharField(max_length=100)
    websiteUrl = models.CharField(max_length=100)
    websiteImage = models.TextField()   #cause we'll put image here
    emailSpecial = EncryptedCharField(max_length=100)
    usernameSpecial = EncryptedCharField(max_length=100)
    passwordSpecial = EncryptedCharField(max_length=100)   #this may need to be changed since we'll probably encrypt it
    userID = models.ForeignKey(User, on_delete=models.CASCADE)  #connection to the user's credentials,
    # not sure whether we have to also add the primary key here

    #magic method - It returns what we want to see when a SavedAccount object is printed.
    def __str__(self):
        return self.websiteName