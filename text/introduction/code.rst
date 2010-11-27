Source 
----------------------------------

All the source for the book is available at the following URL::

    https://github.com/andymckay/cleardjango
    
To check it out, run the following command::

    svn checkout https://cleardjango.googlecode.com/svn/trunk/src
    
This requires a working installation of `Subversion <http://subversion.tigris.org/>`_.

If you are on Windows, the command should work in something like Tortoise SVN. But it is worth noting that pretty much all the examples in this book require the command line to get out of SVN and then run. So you might want to take the time to learn how to do these things from the command line.

The code takes the format of one big Django project. Inside the project, each chapter contains recipes. Those recipes are applications. These terms might not make sense at the moment, but what it does mean is that for each recipe you can: install, configure the database, run the tests and then see the result all in one line of code. No messing about writing out code or anything.

Recipes are accesssed by their recipe number, so for example Recipe 3 will be at src/recipe_03. To run one of these recipes you would use the tools/configure.py command, for example::

    andy@base:~/src$ python tools/configure.py --start 3
    No DJANGO_SETTINGS_MODULE is set, found a settings.py and using that.
    If that is incorrect please specific a DJANGO_SETTINGS_MODULE.

    Creating test database...
    Creating table auth_permission
    Creating table auth_group
    Creating table auth_user
    Creating table auth_message
    Creating table django_content_type
    Creating table django_session
    Creating table django_site
    Creating table recipe_03_todo
    Installing index for auth.Permission model
    Installing index for auth.Message model
    ....
    ----------------------------------------------------------------------
    Ran 4 tests in 0.050s

    OK
    Validating models...
    0 errors found

    Django version 1.1 beta 1, using settings 'settings'
    Development server is running at http://0.0.0.0:8000/
    Quit the server with CONTROL-C.
    
This is good, it means the recipe was installed successfully and the server is now running on port 8000 and ready for use.