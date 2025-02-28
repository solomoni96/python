from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect('posts:index')
        
    return render(request, 'users/register.html', {"form": form})

def user_login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            next_url = request.POST.get('next', 'posts:index')
            return redirect(next_url)

    return render(request, 'users/login.html', {"form": form})

def user_logout(request):
    logout(request)
    return render(request, 'users/logout.html')        
