from django.db import models
from django.core.cache import cache
from django.db.models.signals import post_save, post_delete, post_init

def _key(model, id):
    return "%s.%s" % (model.__name__, id)

timeout = 1

class CarManager(models.Manager):
    def cache(self, id):
        """ Gets the object from the cache """
        car = cache.get(_key(Car, id))
        if not car:
            car = self.get(id=id)
            cache.set(car.key(), car)

        return car
        
class Car(models.Model):
    make = models.CharField(max_length=255)
    objects = CarManager()
    
    def key(self):
        return _key(self.__class__, self.pk)
    
    class Meta:
        # do not use this line in your code, it's only for the book
        app_label = "recipe_09"

def create_cache(sender, **kw):
    cache.set(kw["instance"].key(), kw["instance"], timeout)

def delete_cache(sender, **kw):
    cache.delete(kw["instance"].key())

post_save.connect(create_cache, sender=Car)
post_delete.connect(delete_cache, sender=Car)