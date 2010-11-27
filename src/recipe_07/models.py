from django.db import models
from datetime import datetime

class Todo(models.Model):
    text = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    timestamp = models.DateTimeField()
    
    def save(self, *args, **kw):
        if not self.id:
            self.timestamp = datetime.now()
        super(Todo, self).save(*args, **kw)
        
    class Meta:
        app_label = "recipe_06"
