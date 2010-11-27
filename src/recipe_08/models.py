from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    
    class Meta:
        # do not use this line in your code, it's only for the book
        app_label = "recipe_08"

def create_profile(sender, **kw):
    user = kw["instance"]
    if kw["created"]:
        up = UserProfile(user=user)
        up.save()

post_save.connect(create_profile, sender=User)