Recipe 1: Hello World
--------------------------------------------------

.. topic:: Recipe 1
    
    Run: ``python tools/configure.py -s 1`` to install and run this recipe.

Here's the simplest recipe in the web server world. Printing out "Hello, world!" in the web browser to the visiting user. This can be accomplished in several ways. First the template is written:

.. literalinclude:: ../src/recipe_01/templates/hello.html
   :linenos:

This contains no fancy templating language or code at all, although Django does have a templating language plain text will do. At the moment this just contains the text we want the user to see.

Some web site systems like PHP, allow the server to follow the file structure of your site and render pages in a certain manner. So you might just point the server to hello.html. Django does not do this - instead requiring you to map a URL to a script. There are lots of cunning ways to do this, but the most common way is to explicitly map each incoming URL.

The following file contains some code that might look worrying, but simply put on line 4 it maps the root of the site to the template "hello.html" constructed earlier in this recipe.

.. literalinclude:: ../src/recipe_01/urls.py
   :linenos:

If you visit the site at it's root, for example: http://localhost/ [#f1]_, then you will get the following page:

.. literalinclude:: ../src/recipe_01/templates/hello.html

1. URL mapping
2. Generic views

.. [#f1] This is the first time you've visited the URL in a browser, for this to work you would need Django running and listening on whatever localhost is. This is discussed in the setup section, so if you've skipped ahead to this point and that doesn't work, maybe time to take a step back.
