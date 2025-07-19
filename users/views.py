from django.shortcuts import render
from .models import Admin
from django.db.models import Q
from django.http import HttpResponse

# Create your views here.
def checkadminlogin(request):
    adminuname = request.POST["username"]
    adminpwd = request.POST["password"]

    flag = Admin.objects.filter(Q(username=adminuname) & Q(password=adminpwd))
    print(flag)

    if flag:
        return render(request, "index1.html")
    else:
        return HttpResponse("Login failed")

def insertuser(request):
    if request.method == "POST":
        name = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]


        use = Admin(username=name, email=email, password=password)
        Admin.save(use)
        return render(request, 'login.html')