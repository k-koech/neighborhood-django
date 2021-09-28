from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from ..models import Health,Police
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password


# Create your views here.
@login_required(login_url='/')
def departments(request):
    health=Health.objects.filter(neighborhood__id=request.user.neighborhood.id)
    police=Police.objects.filter(neighborhood__id=request.user.neighborhood.id)
    return render(request,'departments.html',{"health":health, "police":police})