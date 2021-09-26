from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from ..models import Neighborhood, Post
from django.contrib.auth import authenticate,login,logout,login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.hashers import make_password


# Create your views here.
def add_post(request):
    if request.method=="POST":
        title=request.POST.get('title')
        content=request.POST.get('content')
        image=request.FILES.get('image')

        post = Post(title=title, image=image,content=content,neighborhood=request.user.neighborhood, user=request.user)
        post.save()

        messages.add_message(request, messages.SUCCESS, 'Posted successfully!')
        return redirect(add_post)

    else:
        return render(request,'add_post.html')

