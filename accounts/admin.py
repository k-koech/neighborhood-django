from django.contrib import admin
from .models import Users, Post, Neighborhood,Business,Health,Police

"""
    Adding models to an array
"""
models=[Users, Post, Neighborhood,Business,Health,Police]

# Register your models here.
for model in models:
    admin.site.register(model)


"""
    Editing admin page
"""
admin.site.site_header = "The Neighborhood Admin"
admin.site.site_title = "The Neighborhood Admin Portal"
admin.site.index_title = "The Neighborhood Portal"