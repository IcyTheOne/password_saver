from django import forms
from .models import SavedAccount

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
        help_texts = {
            'websiteName': ('Some useful help text.'),
        }
        error_messages = {
            'websiteName': {
                'max_length': ("This writer's name is too long."),
            },
        }