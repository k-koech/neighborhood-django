from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from ..models import Post
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
@login_required(login_url='/')
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

@login_required(login_url='/')
def post(request, id):
    post = Post.objects.get(id=id)
    return render(request,'post.html', {"post":post})

