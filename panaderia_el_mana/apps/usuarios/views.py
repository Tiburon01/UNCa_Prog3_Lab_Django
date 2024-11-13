from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_view(request):
    # if request.user.is_authenticated:
    #     return redirect("usuarios/home.html")
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect(reverse("home"))
        else:
            return render(request, "login.html", {"msj": "Credenciales incorrectas"})
    return render(request, "login.html")

@login_required
def logout_view(request):
    logout(request)
    return render(request, "index.html", {"msj": "Deslogueado"})

# @login_required
# def home(request):
#     return render(request, "home.html")