from django.test import TestCase
from django.core.cache import cache
from models import Car

class CacheTest(TestCase):
    def setUp(self):
        car = Car()
        car.make = "Avensis"
        car.save()
        
        self.car = car
        self.id = car.pk
        
    def testCar(self):
        key = self.car.key()
         
        assert cache.has_key(key)
        assert cache.get(key).make == "Avensis"
        
        self.car.make = "Auris"
        assert cache.get(key).make == "Avensis"
        self.car.save()
        assert cache.get(key).make == "Auris"
        
        self.car.delete()
        assert not cache.has_key(key)