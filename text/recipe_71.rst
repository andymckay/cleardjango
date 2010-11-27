How to: Adding Javascript to the inline fields
-----------------------------------------------------

.. topic:: Recipe 71
    
    Run: ``python tools/configure.py -s 71`` to install and run this recipe.

.. sidebar:: Sponsored Recipe

    This recipe was sponsored by `Blue Fountain Systems Ltd`_. Please contact Clearwind_ if you'd like to sponsor a recipe.

This recipe follows on from the last by adding inline fields to a model in the contrib.admin. This works so long as a user is only going to enter a fixed number each time. Django adds in three extra ingredient inlines for you by default. However, a user may add in more. What we really need is an Javascript solution to add in more rows so the user can keep adding extra rows.

There are two ways to do this. One way is to use the *template* parameter of the admin.TabularInline. You could add in a new template to display the entire inline field set using this. You'd want to go grab the inline template and then place it in your project to do this. Then you could customize it to add a button and some JavaScript. You can see this in the *templates* directory of this recipe.

I didn't choose that way because it involves the copy and paste of large amounts of Django template code. Remember template code can change and you'll need to maintain that template code across versions. The only real advantage of doing that copy and paste is to include a snippet of JavaScript and a bit of HTML. The JavaScript shouldn't be in the template and should be in an external file anyway. So this is really a less desirable solution.

You'll see what I chose to do instead in the *media* folder of this recipe. Take a look at the *add_tabular_inline.js* file. This uses jQuery to add an add button and then clone the last row of the inlines.

Let's setup the JavaScript. You can add custom JavaScript using the Media class inside RecipeAdmin. This particular one pulls in jQuery from Google's servers and then the JavaScript from our recipe [#f1]_.

.. literalinclude:: ../src/recipe_71/admin.py
   :language: python
   :linenos:
   :lines: 24-29

The JavaScript creates a button and then binds a clone event to it. This works with the *TabularInline*. A *StackedInline* would require slightly different code. This isn't much longer at all compared to the embedding in the template version:

.. literalinclude:: ../src/recipe_71/media/add_tabular_inline.js
   :language: javascript
   :linenos:

To facilitate the addition and removal of inlines, Django provides an input field that calculates the total number of forms in the formset. When you insert or remove forms, you need to alter that number so that Django knows to process the data. This is the *id_recipe-TOTAL_FORMS* input. Line 24 of the above code increments that value.

This is based on the work in this blog. [#f2]_

.. [#f1] See notes in MEDIA_URL and serving static content, something this recipe does on start up.
.. [#f2] http://www.arnebrodowski.de/blog/507-Add-and-remove-Django-Admin-Inlines-with-JavaScript.html
.. _Clearwind: http://www.clearwind.ca
.. _Blue Fountain Systems Ltd: http://www.bluefountain.com/