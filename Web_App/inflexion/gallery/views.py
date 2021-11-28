from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .decorators import unauthenticated, allowed_user
from .forms import NewUserForm
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


def index(request):
    return render(request, "gallery/index.html")



@allowed_user(roles_allowed=['admin'])
def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("gallery:index")

    form = NewUserForm()
    return render(request, "gallery/user.html",
                  {"register_form": form})


@unauthenticated
def log_in(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                if user.groups.all()[0].name == 'admin':
                    return render(request, 'gallery/index.html',
                                  {"user": user, "name": "admin"})
                else:
                    return render(request, 'gallery/index.html',
                                  {"user": user,"name": "user"})
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, "gallery/log_in.html", context={"login_form": form})


@login_required
def log_out(request):
    logout(request)
    return redirect('gallery:index')


def userpage(request):
    images = Image.objects.all()
    return render(request, "gallery/profile.html",
                  context)
