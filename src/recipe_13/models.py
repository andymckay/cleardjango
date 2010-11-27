from django.db import models
from django.contrib.auth.models import User

class BankAccount(models.Model):
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    number = models.CharField(max_length=10)
    
    class Meta:
        app_label = "recipe_13"
        
class Log(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    
    class Meta:
        app_label = "recipe_13"
        
def log(sender, instance, **kw):
    new = Log()
    new.save()
    
models.signals.pre_save.connect(log, sender=BankAccount)        