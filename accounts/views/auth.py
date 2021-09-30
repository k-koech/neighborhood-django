import random
import string
from django.core.mail import send_mail

from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from ..models import Business, Neighborhood, Users,Post
from django.contrib.auth import authenticate,login,logout,login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.hashers import make_password

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        posts= Post.objects.filter(neighborhood__id=request.user.neighborhood.id)
        return render(request,'index.html',{"posts":posts})
    else:
        return render(request,'index.html')

@login_required(login_url='/')
def business(request):
    """BUSINESS VIEW"""
    business= Business.objects.filter(neighborhood=request.user.neighborhood.id)
    return render(request,'business.html',{"businesses":business})

@login_required(login_url='/')
def search(request):
    """BUSINESS SEARCH"""
    if request.method=="POST":
        search=request.POST.get('search')
        business= Business.objects.filter(neighborhood=request.user.neighborhood.id, name__contains=search)
        return render(request,'business.html',{"businesses":business})
    else:
        return redirect(index)



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
            messages.add_message(request, messages.ERROR, 'ID exist!')
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

                messages.add_message(request, messages.SUCCESS, 'Registered successfully!')
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
            return redirect(index)
 
        else:
            messages.add_message(request, messages.ERROR, 'Invalid Credentials!')
            return redirect(signIn)

     else:
        return render(request, "login.html")

""" LOGOUT VIEW """
def signOut(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, 'Logout success')
    return redirect(signIn)

@login_required(login_url='/')
def profile(request):   
    """PROFILE """
    if request.method=="POST":
        user=Users.objects.get(id=request.user.id)

        user.name=request.POST.get('name')
        user.profile_photo=request.FILES['profile_photo']
        user.about_me=request.POST['about_me']
        user.phone=request.POST.get('phone_number')
        
        user.save()

        messages.add_message(request, messages.SUCCESS, 'Profile  Updated')
        return redirect(profile)
     
    else:
        neighborhoods=Neighborhood.objects.all()
        return render(request, "profile.html",{"neighborhoods":neighborhoods})


"""FORGOT PASSWORD"""
def forgotpassword(request):
    if request.method=="POST":
        email= request.POST.get('email')
        email_exist=Users.objects.filter(email=email).count()
        
        if email_exist<1:
            messages.add_message(request, messages.ERROR, 'Email does not exist!')
            return redirect(forgotpassword)

        elif email_exist>0:
            user=Users.objects.get(email=email)
            # generate password
            letters = string.ascii_lowercase
            new_password=''.join(random.choice(letters) for i in range(10))
            user.password=make_password(new_password)
            user.save()
            send_mail('New Password',
                'Your new password is '+new_password+". Ensure that you update your password after login.",
                'Neighborhood',
                [email],
                fail_silently=False,
            )
            messages.add_message(request, messages.SUCCESS, 'Email sent successfully!')
            return redirect(forgotpassword)

    else:
        return render(request, "forgot_password.html")


"""UPDATE PASSWORD"""
@login_required(login_url='/')
def updatepassword(request):
    password=request.POST.get('password')
    confirm_password=request.POST.get('confirm_password')
    if password!=confirm_password:
        messages.add_message(request, messages.ERROR, "Password doesn't match!!")
        return redirect(profile)
       
    else:
        user=Users.objects.get(id=request.user.id)
        user.password = password=make_password(password)
        user.save()
        messages.add_message(request, messages.SUCCESS, "Password updated successfully!!")
        return redirect(profile)

@login_required(login_url='/')
def update_neighborhood(request):
    """Neighborhood"""
    if request.method=="POST":
        user=Users.objects.get(id=request.user.id)
        user.neighborhood=Neighborhood.objects.get(id=request.POST.get('neighborhood'))

        user.save()

        messages.add_message(request, messages.SUCCESS, 'Neighborhood  Updated')
        return redirect(profile)