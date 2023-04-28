from django.db import models
import uuid
from users.models import Profile
# Create your models here.


class Project(models.Model):
    # one to many relation ship (one profile many projects)
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # since this image is in images folder we dont need to specify path for it, eg, if it was in a folder named profile picure then our path would be "profile picture/default.jpg"
    featured_image = models.ImageField(
        null=True, blank=True, default="default.jpg")
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    # you do not need to add the Tag in quote if the Tag model is above the Project model but it is not above the project model in this case so we need to add it within a quote
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    # gives date and a time stamp
    created = models.DateTimeField(auto_now_add=True)
    # auto_now_add=True generates a timestamp whenever a new project entry/model instance is created
    # uuid4 is an encoding type, unique=True means no other value in the database can have the  same number
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
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
        # we can reference this vote by 'up' in db but 'Up Vote' is what it's gonna be displayed as to the users
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )

    # owner =
    # [on_delete=models.CASCADE] will delete all the reviews if the project is deleted
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.value


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name
