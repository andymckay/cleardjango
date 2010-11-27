from django.db import models

class Todo(models.Model):
    text = models.CharField(max_length=255)
    
    class Meta:
        app_label = "recipe_13"