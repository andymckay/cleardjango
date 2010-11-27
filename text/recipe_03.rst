Recipe 3: A first model
--------------------------------------------------

.. topic:: Recipe 3
    
    Run: ``python tools/configure.py -s 3`` to install and run this recipe.

Of course writing something that returns a bit of Python to the user is all very well, but really we need something that reads and writes to a database. For this Django has models. Models are classes in Python that explicitly declare what data is persisted to the database.

A model lives in a *models.py* file [#f1]_. It inherits from *django.db.models* and will look something like this:

.. literalinclude:: ../src/recipe_03/models.py
   :linenos:
   :lines: 1-4

The name of this model is called *Todo* and it has no fields at this time. This means it doesn't have any custom data it. Perhaps "Chocolate Teapot" [#f2]_ would be a more useful name for this model.

When you install this model, either via the recipe command or via syncdb, Django will create a table called *recipe_03_todo*. There's no need to write any SQL to create tables or columns, Django has done all that for you. There are two easy ways to easy what Django has done for you from the *manage.py* command. A very useful command is sqlall which shows you the SQL that was used to create the tables.

For this recipe it looks like this:

.. code-block:: sql
    :linenos:
    
    BEGIN;
    CREATE TABLE "recipe_03_todo" (
        "id" integer NOT NULL PRIMARY KEY
    )
    ;
    COMMIT;

You'll note that it has created and *id* column for you. This is the primary key for the table. It doesn't have to be *id*, but if you don't specify it on a field Django will add it in for you [#f3]_.

This then is the simplest model you can have. Next we'll add in some fields.

.. [#f1] It doesn't have to be a file, it could be a directory called models. Inside that directory there has to be an *__init__.py* file that subsequently can import multiple other Python modules. As long as Python has something called models it can import, it's happy.
.. [#f2] If you are not British, you might need to Google this term.
.. [#f3] http://docs.djangoproject.com/en/dev/ref/models/fields/#primary-key
