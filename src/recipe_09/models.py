from django.db import models
from django.core.cache import cache
from django.db.models.signals import post_save, post_delete

def _key(model, id):
    return "%s.%s" % (model.__name__, id)

class Car(models.Model):
    make = models.CharField(max_length=255)
    
    def key(self):
        return _key(self.__class__, self.pk)
    
    class Meta:
        # do not use this line in your code, it's only for the book
        app_label = "recipe_09"

def create_cache(sender, **kw):
    cache.set(kw["instance"].key(), kw["instance"])

def delete_cache(sender, **kw):
    cache.delete(kw["instance"].key())

post_save.connect(create_cache, sender=Car)
post_delete.connect(delete_cache, sender=Car)