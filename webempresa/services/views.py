from django.shortcuts import render
from .models import Service


def services(request):
    servics = Service.objects.all()
    return render(request, "services/services.html", {'servics': servics})
