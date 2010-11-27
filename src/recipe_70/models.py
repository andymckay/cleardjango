from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __unicode__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    amount = models.CharField(max_length=255)
    
    recipe = models.ForeignKey(Recipe, related_name="recipe")
    other_recipe = models.ForeignKey(Recipe, related_name="other_recipe", blank=True, null=True)
