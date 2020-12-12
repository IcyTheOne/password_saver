from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required as Login_required
from django.contrib.auth.models import User
from .models import SavedAccount
from .forms import VaultAccountForm


websiteImages = {
    'linkedin':'https://www.kinesisinc.com/wp-content/uploads/2020/04/linkedin-101-hero@2x.png',
    'discord':'https://fiverr-res.cloudinary.com/images/t_main1,q_auto,f_auto,q_auto,f_auto/gigs/134280614/original/9e46d93ff60530cf5f07118c6f961c68294179b9/create-an-icon-for-a-discord.jpg',
    'youtube':'https://9to5google.com/wp-content/uploads/sites/4/2018/09/youtube_logo_dark.jpg?quality=82&strip=all',
    'facebook':'https://lmplumbersworcester.co.uk/wp-content/uploads/2020/10/fa-kIN-U4042808631756D-624x385@Las-Provincias.jpg',
    'default_image':'vault/lock.png',
}


# Create your views here.
@Login_required
def home(request):
    logedinUser = request.user  # Getting the currently loged in user
    logedinUserSavedAccounts = SavedAccount.objects.filter(userID=logedinUser.pk)   # Getting saved accounts for currently loged-in user.

    context = {
        'title':'Home',
        'savedAccounts': logedinUserSavedAccounts,
        'websiteImages':websiteImages
    }

    if request.method == 'POST':
        return storeVaultAccount(request, logedinUser)
    else:
        form = VaultAccountForm()
        context['vaultAccountForm'] = form # Passing the created form through the context dict to the html.
    return render(request, 'vault/home.html', context)


def storeVaultAccount(request, logedinUser):
    form = VaultAccountForm(request.POST)
    if form.is_valid():
        newVaultAccount = form.save(commit=False)  # Create, but don't save the new VaultAccount instance. This instance only contains data received from the form, but to be a valid insertion to the database an image url and a userID must be specified. 
        newVaultAccount.userID = logedinUser # Add logedin user entry for the VaultAccounts table.
        websiteName = form.cleaned_data['websiteName']
        # email = form.cleaned_data['emailSpecial']

        if websiteName in websiteImages.keys(): # Checking if the mentioned website name corresponds to a url image.
            newVaultAccount.websiteImage = websiteImages[websiteName]
        else:
            newVaultAccount.websiteImage = websiteImages['default_image']

        newVaultAccount.save()

        messages.success(request,f'Account Credentials saved for {websiteName}!')

        return redirect('vault-home')