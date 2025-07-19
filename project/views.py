from django.shortcuts import render

def loginfunction(request):
    return render(request,"login.html")

def adminfunction(request):
    return render(request,"index.html")


def admin1function(request):
    return render(request,"index1.html")


def signupfunction(request):
    return render(request,"signup.html")



