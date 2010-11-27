from django import forms

from recipe_72.models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe

def ingredient_form_callback(instance, field, *args, **kw):
    if field.name == "other_recipe":
        if instance:
            return field.formfield(queryset=Recipe.objects.exclude(pk=instance.pk), **kw)
    return field.formfield(**kw)
