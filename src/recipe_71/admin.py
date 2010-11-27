from django.contrib import admin
from django.utils.functional import curry

from models import Recipe, Ingredient
from forms import ingredient_form_callback
    
class IngredientInline(admin.TabularInline):
    model = Ingredient
    fk_name = "recipe"

    def get_formset(self, request, obj=None, **kwargs):
        kwargs["formfield_callback"] = curry(ingredient_form_callback, obj)
        return super(IngredientInline, self).get_formset(request, obj, **kwargs)
    
class IngredientAdmin(admin.ModelAdmin):
    pass
        
class RecipeAdmin(admin.ModelAdmin):
    inlines = [
        IngredientInline
    ]
    list_display = ("name",)
    
    class Media:
        js = (
            "http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js",
            "/recipe_media/add_tabular_inline.js",
            )

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)