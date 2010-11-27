from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.forms.models import inlineformset_factory
from django.utils.functional import curry

from recipe_72.models import Recipe, Ingredient
from recipe_72.forms import RecipeForm, ingredient_form_callback

def add(request):
    IngredientFormSet = inlineformset_factory(Recipe, Ingredient, 
                fk_name="recipe", 
                formfield_callback=curry(ingredient_form_callback, None))
    
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        formset = IngredientFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            recipe = form.save()
            formset = IngredientFormSet(request.POST, instance=recipe)            
            formset.save()
            return redirect("/edit/%s" % recipe.id)
    else:
        form = RecipeForm()
        formset = IngredientFormSet()
    
    return render_to_response("recipe_72_add.html", {"form":form, "formsets":formset})

def edit(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    IngredientFormSet = inlineformset_factory(Recipe, Ingredient, 
        fk_name="recipe", 
        formfield_callback=curry(ingredient_form_callback, recipe))
    
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        formset = IngredientFormSet(request.POST, instance=recipe)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect("/edit/%s" % recipe.id)
    else:
        form = RecipeForm(instance=recipe)
        formset = IngredientFormSet(instance=recipe)

    return render_to_response("recipe_72_edit.html", {"form":form, "formsets":formset, "recipe":recipe})
    
