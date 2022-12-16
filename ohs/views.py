from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from ohs.forms import Register, login_form
from ohs.models import Login


# Create your views here.
def index(request):
    return render(request, "index.html")


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("uname")
        password = request.POST.get("pass")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect("indexx")
        else:
            messages.info(request, "Invalid Credentials")
    return render(request, "login.html")


def indexx(request):
    return render(request, "indexx.html")


def registration(request):
    return render(request, "registration.html")


def regiworker(request):
    return render(request, "regiworker.html")


def dashboardworker(request):
    return render(request, "dashboardworker.html")


def dashboardcustomer(request):
    return render(request, "dashboardcustomer.html")


#
# def logincu(request):
#     return render(request, "logincu.html")

def customer_registration(request):
    form1 = login_form()
    form2 = Register()
    if request.method == 'POST':
        form1 = Login(request.POST)
        form2 = Register(request.POST, request.FILES)

        if form1.is_valid() and form2.is_valid():
            a = form1.save(commit=False)
            a.is_customer = True
            a.save()
            user1 = form2.save(commit=False)
            user1.user = a
            user1.save()
            return redirect("login_page")
    return render(request, "customer.html", {'form1': form1, 'form2': form2})
# def customer(request):
#     return render(request, "customer.html")
def workers(request):
    return render(request, "workers.html")


