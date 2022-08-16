from django.shortcuts import render, redirect

# Create your views here.
def login_page(request):
    return render(request, "login.html", context = None)

def index(request):
    return redirect(login_page)

def dashboard(request):
    return render(request, "dashboard.html", context = None)