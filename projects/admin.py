from django.contrib import admin

# Register your models here.
from .models import Project, Review, Tag # importing model
# even after we created model in models.py file, it will not show in django admin
# we need to register it first
admin.site.register(Project) # registering the model
admin.site.register(Review)
admin.site.register(Tag) 
