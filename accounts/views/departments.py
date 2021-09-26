from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from ..models import Neighborhood, Users
from django.contrib.auth import authenticate,login,logout,login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.hashers import make_password


# Create your views here.
def departments(request):
    return render(request,'portfolio-details.html')