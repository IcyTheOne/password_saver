from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()  # aaand this is how new user is added to DB
            username = form.cleaned_data.get('username')
            messages.success(request,
                             f'Account created for {username}!')  # gotta fix this cause its fucking up the view
            return redirect('vault-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
