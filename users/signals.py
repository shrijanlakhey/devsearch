from django.db.models.signals import post_save, post_delete
# post_save = this method is gonna trigger anytime after a model is saved
from django.dispatch import receiver
from django.contrib.auth.models import User
from . models import Profile

# sender = model taht actually sends it, instance = the instance/object of the model that actually triggered it, created = T or F value that lets us know if a user or model was added to the b or it was simply savced again

# @receiver is a decorator
# @receiver(post_save, sender=Profile)
def createProfile(sender, instance, created, **kwargs):
    if created:  # checks if this is the first instance, return true if it is first instance
        user = instance  # sender is gonna be an instance i.e User
        # everytime a user is created, their profile is also created
        profile = Profile.objects.create(
            user=user,  # a profile needs a user so connecting the new profile to the user that just triggered this
            username=user.username,
            email=user.email,
            name=user.first_name,
        )


# delete the corresponding user everytime a profile is deleted
def deleteUser(sender, instance, **kwargs):
    user = instance.user  # Profile is the instance
    user.delete()


# everytime a User model gets created, a profile will be created too
post_save.connect(createProfile, sender=User)

post_delete.connect(deleteUser, sender=Profile)
