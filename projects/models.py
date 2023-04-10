from django.db import models
import uuid
# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True) # gives date and a time stamp
    # auto_now_add=True generates a timestamp whenever a new project entry/model instance is created
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False) # uuid4 is an encoding type, unique=True means no other value in the database can have the  same number
    # no need to create an id field whenever we are inheriting from 'models.Model' because django creates it by itself, by default it is of int type
    # but it is recommened to use uuid 
# null=True, blank=True means that the user is able to submit the form even if the field (eg, description) is empty or blank 
# in django, by default null value is False which means the fields should not be left empty