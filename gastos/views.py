from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request,"gastos\home.html")

def quedada(request):
    
    nombre = request.GET.get("nombre")
    gasto = request.GET.get("gasto")
    importe = request.GET.get("importe")

    return render(request,"gastos\quedada.html", {"nombre": nombre,"gasto":gasto,"importe":importe})

def password(request):
    
    characters = list("abcdefghijklmnopqrstuvwxyz")

    if request.GET.get("uppercase"):
        characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

    if request.GET.get("special"):
        characters.extend(list("!·$%&/("))
    
    if request.GET.get("numbers"):
        characters.extend(list("123456789"))

    lenght = int(request.GET.get("lenght", 6))
    thepassword = ''
    
    for x in range(lenght):
        thepassword += random.choice(characters)

    return render(request,"gastos\password.html", {'password':thepassword})
