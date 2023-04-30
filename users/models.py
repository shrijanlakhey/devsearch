from django.db import models
from django.contrib.auth.models import User
import uuid

from django.db.models.signals import post_save, post_delete
# post_save = this method is gonna trigger anytime after a model is saved
from django.dispatch import receiver

# Create your models here.


class Profile(models.Model):
    # user will have one to one rleationship with User model(dajngo's built in model),
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    # every single user in the db will have a profile and every profile will ahve a user and profiel will get automaticlly generated everytime a user is created
    # 'on_delete=models.CASCADE', everytime user is deleted, hs porfile is also deleted
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    short_intro = models.CharField(max_length=500, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(
        blank=True, null=True, upload_to='profiles/', default='profiles/user-default.png')

    social_github = models.CharField(max_length=200, blank=True, null=True)
    social_twitter = models.CharField(max_length=200, blank=True, null=True)
    social_linkedin = models.CharField(max_length=200, blank=True, null=True)
    social_youtube = models.CharField(max_length=200, blank=True, null=True)
    social_website = models.CharField(max_length=200, blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        # if we want to use a number here then we need to wrap that in a string method (str)
        return str(self.username)


class Skill(models.Model):
    # 'Profile' is the parent and 'Skill' is the child
    owner = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)


# sender = model taht actually sends it, instance = the instance/object of the model that actually triggered it, created = T or F value that lets us know if a user or model was added to the b or it was simply savced again

# @receiver is a decorator
@receiver(post_save, sender=Profile)
def profileUpdated(sender, instance, created, **kwargs):
    print("Profile Saved!")
    print("Instance:", instance)
    print("Created:", created)


# delete the corresponding user everytime a profile is deleted
def deleteUser(sender, instance, **kwargs):
    print("Deleting user...")


# everytime a save method is called in the model 'Profle', after the save method is complete the profileUpdated method will be triggered
# post_save.connect(profileUpdated, sender=Profile)

# post_delete.connect(deleteUser,sender=Profile)


