from django.db import models
from datetime import datetime

class Todo(models.Model):
    text = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    timestamp = models.DateTimeField()
    creation = models.DateTimeField()
    
    class Meta:
        app_label = "recipe_04"
 
def add_date(sender, instance, **kw):
    instance.timestamp = datetime.now()
    if not instance.id:
        instance.creation = datetime.now()
           
models.signals.pre_save.connect(add_date, sender=Todo)