from django.contrib import admin
from django.urls import path
from .views.auth import dashboard, index, profile, register,signIn, signOut,update_neighborhood
# from .views.projects import add_project, fouroffour_not_found,profile, profile_photo
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', index, name='index'),
    path('register', register, name='register'),
    path('login', signIn, name='login'),
    path('signOut', signOut, name='signOut'),
 
    path('dashboard', dashboard, name='dashboard'),
    path('profile', profile, name='profile'),
    path('profile/neighborhood', update_neighborhood, name='update_neighborhood'),

    # path('profile_photo', profile_photo, name='profile_photo'),
    # path('add_project', add_project, name='add_project'),
    # path('sites/<id>', project, name='project'),
    #  path('search', search, name='search'),
    # path('project/<id>', project, name='project'),
    # path('404', fouroffour_not_found, name='404'),


    # path('project/delete/<id>', delete_project, name='delete_project'),
   
]
urlpatterns += staticfiles_urlpatterns()
