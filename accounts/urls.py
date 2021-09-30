from django.contrib import admin
from django.urls import path
from .views.auth import index, profile, register,signIn,business, signOut,update_neighborhood, search,forgotpassword, updatepassword
from .views.departments import departments
from .views.post import add_post, post
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', index, name='index'),
    path('register', register, name='register'),
    path('login', signIn, name='login'),
    path('signOut', signOut, name='signOut'),
    path('forgotpassword', forgotpassword, name='forgotpassword'),
    path('updatepassword', updatepassword, name='updatepassword'),
 
    path('business', business, name='business'),
    path('profile', profile, name='profile'),
    path('profile/neighborhood', update_neighborhood, name='update_neighborhood'),

    path('departments', departments, name='departments'),
    path('add_post', add_post, name='add_post'),

    path('post/<id>', post, name='post'),
     path('search', search, name='search'),
     
]
urlpatterns += staticfiles_urlpatterns()
