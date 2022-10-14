from django.shortcuts import render

from accounts.forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
    else:
        form = CustomUserCreationForm()
    context ={
        'form' : form
    }
    return render(request, 'accounts/signup.html', context)