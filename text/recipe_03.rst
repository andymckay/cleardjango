Recipe 3: A first model
--------------------------------------------------

.. topic:: Recipe 3
    
    Run: ``python tools/configure.py -s 3`` to install and run this recipe.

Next, let's talk to a database. For this Django has models. Models are classes in Python that explicitly declare what data is persisted to the database.

A model lives in a *models.py* file [#f1]_. It inherits from *django.db.models*. Here is an exmample:

.. literalinclude:: ../src/recipe_03/models.py
   :linenos:
   :lines: 1-4

The name of this model is called *Todo* and it has no fields at this time. This means it doesn't have any custom data in it.

When you install this model, either via the recipe command or via *syncdb* [#f2]_, Django will create a table called *recipe_03_todo*. There's no need to write any SQL to create tables or columns, Django has done all that for you.

One way to see what SQL Django will create for you is the *manage.py* *sqlall* [#f3]_ command. For this recipe it looks like this:

.. code-block:: sql
    :linenos:
    
    BEGIN;
    CREATE TABLE "recipe_03_todo" (
        "id" integer NOT NULL PRIMARY KEY
    )
    ;
    COMMIT;

You'll note that it has created and *id* column for you. This is the primary key for the table. It doesn't have to be *id*, but if you don't specify it on a field Django will add it in for you [#f4]_.

In this recipe we've:

1. Created a simple model and some tables in the database.

At this point nothing is visible in the browser, we haven't hooked anything up.

.. [#f1] It doesn't have to be a file, it could be a directory called models. Inside that directory there has to be an *__init__.py* file that subsequently can import multiple other Python modules. As long as Python has something called models it can import, it's happy.
.. [#f2] http://docs.djangoproject.com/en/dev/ref/django-admin/#syncdb
.. [#f3] http://docs.djangoproject.com/en/dev/ref/django-admin/#sqlall
.. [#f4] http://docs.djangoproject.com/en/dev/ref/models/fields/#primary-key
