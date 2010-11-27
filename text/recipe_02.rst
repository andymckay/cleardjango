Recipe 2: Hello World via Python
--------------------------------------------------

.. topic:: Recipe 2
    
    Run: ``python tools/configure.py -s 2`` to install and run this recipe.

Recipe 1 was pretty simple and didn't have any real opportunity for dynamic content. It went straight from a request to a
very simple HTML template. Let's expand that a little by taking the request, doing some Python processing and return something dynamic.

The first step of this is to put in a *view*. A *view* is just Django's name for a Python callable that takes a request object and outputs a response that will be passed back to the web server. First we need to create a view:

.. literalinclude:: ../src/recipe_02/views.py
   :linenos:

This view is very simple. All views are passed at least one parameter, request, this encapsulates data about the request that the web server has received. We then use a django shortcut module method [#f1]_ called render_to_response. This method takes a template name and when executed will find the template, execute it and return the result back to the browser.

The final change is to our view, we are no longer pointing the URL to the template via a generic view as we did in recipe 1, but rather pointing at a view. Our urls.py is now changed too:

.. literalinclude:: ../src/recipe_02/urls.py
   :linenos:

If you visit the site at it's root, for example: http://localhost/, then you will get the following page:

.. literalinclude:: ../src/recipe_01/templates/hello.html

The key changes here are:

1. We've created a view to process the request
2. We've changed the urls to use that view

So with that in mind, let's hope over to databases.

.. [#f1] http://docs.djangoproject.com/en/dev/topics/http/shortcuts/
