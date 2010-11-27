from models import Recipe

def ingredient_form_callback(instance, field, *args, **kw):
    if field.name == "other_recipe":
        if instance:
            return field.formfield(queryset=Recipe.objects.exclude(pk=instance.pk), **kw)
    return field.formfield(**kw)
