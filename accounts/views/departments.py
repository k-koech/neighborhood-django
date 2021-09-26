from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from ..models import Health,Police
from django.contrib.auth import authenticate,login,logout,login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.hashers import make_password


# Create your views here.
# @login_required("/")portfolio
def departments(request):
    health=Health.objects.filter(neighborhood__id=request.user.neighborhood.id)
    police=Police.objects.filter(neighborhood__id=1)
    return render(request,'departments.html',{"health":health, "police":police})