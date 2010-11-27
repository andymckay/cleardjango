from django.test import TestCase
from models import UserProfile
from django.contrib.auth.models import User

class UserTest(TestCase):
    def testUser(self):
        u = User.objects.create(
             username='admin',
             email='andy@clearwind.ca')

        u.save()
        
        assert u.get_profile()
        assert User.objects.count() == 1
        assert UserProfile.objects.count() == 1
        
        # if we change something and save it
        u.password = "testing"
        u.save()
        
        # we still only have one profile
        assert u.get_profile()
        assert User.objects.count() == 1
        assert UserProfile.objects.count() == 1
        
        # if we delete it, back to zero
        u.delete()
        
        assert User.objects.count() == 0
        assert UserProfile.objects.count() == 0
        