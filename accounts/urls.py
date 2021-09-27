from django.contrib import admin
from django.urls import path
from .views.auth import index, profile, register,signIn,business, signOut,update_neighborhood
from .views.departments import departments
from .views.post import add_post, post
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', index, name='index'),
    path('register', register, name='register'),
    path('login', signIn, name='login'),
    path('signOut', signOut, name='signOut'),
 
    path('business', business, name='business'),
    path('profile', profile, name='profile'),
    path('profile/neighborhood', update_neighborhood, name='update_neighborhood'),

    path('departments', departments, name='departments'),
    path('add_post', add_post, name='add_post'),

    path('post/<id>', post, name='post'),
    #  path('search', search, name='search'),
    # path('project/<id>', project, name='project'),
    # path('404', fouroffour_not_found, name='404'),


    # path('project/delete/<id>', delete_project, name='delete_project'),
   
]
urlpatterns += staticfiles_urlpatterns()
