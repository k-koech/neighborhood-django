from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from ..models import Neighborhood, Users,Post
from django.contrib.auth import authenticate,login,logout,login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.hashers import make_password


# Create your views here.
def index(request):
    posts= Post.objects.filter(neighborhood__id=request.user.neighborhood.id)
    return render(request,'index.html',{"posts":posts})

def dashboard(request):
    """dashboard view"""
    posts= Post.objects.all()
    return render(request,'dashboard.html',{"posts":posts})
    # return render(request,'dashboard.html')

""" USER REGISTRATION VIEW """  
def register(request):   
    if request.method=="POST":
        id_number=request.POST.get('id_number')
        email=request.POST.get('email')
        name=request.POST.get('name')

        neighborhood=Neighborhood.objects.get(id=request.POST.get('neighborhood'))

        password=request.POST.get('password')
        confirm_password=request.POST.get('password-repeat')

        id_numbers=Users.objects.filter(id_number=id_number).count()
        email_exist=Users.objects.filter(email=email).count()

        if id_numbers>0:
            messages.add_message(request, messages.ERROR, 'Username exist!')
            return redirect(register)

        elif email_exist>0:
            messages.add_message(request, messages.ERROR, 'Email exist!')
            return redirect(register)

        else:
            if password!=confirm_password:
                messages.add_message(request, messages.ERROR, 'Username exist!')
                return redirect(register)
            else:
                user = Users(name=name, email=email,id_number=id_number,neighborhood=neighborhood, password=make_password(password))
                user.save()

                messages.add_message(request, messages.SUCCESS, 'Registereed successfully!')
                return redirect(signIn)
     
    else:
        neighborhoods=Neighborhood.objects.all()
        return render(request, "register.html", {"neighborhoods":neighborhoods})

""" LOGIN VIEW """
def signIn(request):
     if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        user= authenticate(email=email, password=password)
        print(email)
        print(password)
        if user is not None:
            login(request,user )
            messages.add_message(request, messages.SUCCESS, 'Logged in successfully')
            return redirect(dashboard)
 
        else:
            messages.add_message(request, messages.ERROR, 'Invalid Credentials!')
            return redirect(signIn)

     else:
        return render(request, "login.html")

""" LOGOUT VIEW """
def signOut(request):
    logout(request)
    # messages.add_message(request, messages.SUCCESS, 'Logout successfully!')
    return redirect(index)

def profile(request):   
    """PROFILE """
    if request.method=="POST":
        user=Users.objects.get(id=request.user.id)

        user.name=request.POST.get('name')
        user.profile_photo=request.FILES['profile_photo']
        user.phone=request.POST.get('phone_number')
        
        user.save()

        messages.add_message(request, messages.SUCCESS, 'Profile  Updated')
        return redirect(profile)
     
    else:
        neighborhoods=Neighborhood.objects.all()
        return render(request, "profile.html",{"neighborhoods":neighborhoods})


def update_neighborhood(request):
    """Neighborhood"""
    if request.method=="POST":
        user=Users.objects.get(id=request.user.id)
        user.neighborhood=Neighborhood.objects.get(id=request.POST.get('neighborhood'))

        user.save()

        messages.add_message(request, messages.SUCCESS, 'Neighborhood  Updated')
        return redirect(profile)