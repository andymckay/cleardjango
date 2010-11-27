from django.db import models

class Todo(models.Model):
    text = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    timestamp = models.DateTimeField()
    
    class Meta:
        app_label = "recipe_03"
