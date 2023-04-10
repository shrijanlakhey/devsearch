from django.db import models
import uuid
# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True) # you do not need to add the Tag in quote if the Tag model is above the Project model but it is not above the project model in this case so we need to add it within a quote
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True) # gives date and a time stamp
    # auto_now_add=True generates a timestamp whenever a new project entry/model instance is created
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False) # uuid4 is an encoding type, unique=True means no other value in the database can have the  same number
    # no need to create an id field whenever we are inheriting from 'models.Model' because django creates it by itself, by default it is of int type
    # but it is recommened to use uuid 
    # null=True, blank=True means that the user is able to submit the form even if the field (eg, description) is empty or blank 
    # in django, by default null value is False which means the fields should not be left empty


    # anytime we access the model and not it's attribute, it will be output with the title value
    def __str__(self):
        return self.title
    
class Review(models.Model):
    # VOTE_TYPE is a tuple
    VOTE_TYPE = (
        ('up', 'Up Vote'), # we can reference this vote by 'up' in db but 'Up Vote' is what it's gonna be displayed as to the users 
        ('down', 'Down Vote'),
    )
    
    # owner = 
    project = models.ForeignKey(Project, on_delete=models.CASCADE) # [on_delete=models.CASCADE] will delete all the reviews if the project is deleted
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True) 
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False) 

    def __str__(self):
        return self.value
    
class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True) 
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False) 

    def __str__(self):
        return self.name
