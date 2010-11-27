Recipe 4: A first model, with fields
--------------------------------------------------
   
.. topic:: Recipe 4
    
    Run: ``python tools/configure.py -s 4`` to install and run this recipe.

Let's add some fields to the last recipe to make it more interesting. A field is the definition of the column in the database. So let's give our *Todo* model the following fields:

* *text* some details about the todo item eg: "Go get milk"

* *completed* a Yes/No flag to see if the todo has been completed

* *timestamp* a timestamp for when the todo has been completed

This would change the model to look like the following:

.. literalinclude:: ../src/recipe_04/models.py
   :linenos:
   :lines: 1-6

There's lots of fields available to you and the full reference of them can be found online [#f1]_. It would be fantastically boring to relist them all here, so I won't bother. But basically you can see we have *CharField*, a *BooleanField* and a *DateTimeField* which all correspond to the data required.

If you reinstall this recipe and use the *sqlall* command, you can see the SQL that gets created [#f2]_:

.. code-block:: sql
    :linenos:

    BEGIN;
    CREATE TABLE "recipe_04_todo" (
        "id" integer NOT NULL PRIMARY KEY,
        "text" varchar(255) NOT NULL,
        "completed" bool NOT NULL,
        "timestamp" datetime NOT NULL
    )
    ;
    COMMIT;

So we've got a model, how do we create a record in the database of this?

1. Create an instance of the class.
2. Assign values to the fields.
3. Call save method on the class.

For example:

.. code-block:: python
    :linenos:

    from datetime import datetime

    todo = Todo()
    todo.text = "Get some milk"
    todo.timestamp = datetime.now()
    todo.save()
   
The assignment of values to the object matches the fields. If the field is called *text* then you assign to *text* (line 4). Calling save performs all the necessary SQL inserts into the database.

In this model, we've set a default value for *completed* to be *False*. So we didn't bother assigning the value for *completed*.

But we did set one for *timestamp* [#f3]_. This is a required field and if you don't assign it, for example:

.. code-block:: python
    :linenos:
    
    todo = Todo()
    todo.text = "Get some milk"
    todo.save()

You'll get an error::
    
      File "/usr/lib/python2.5/site-packages/django/db/backends/sqlite3/base.py", line 193, in execute
        return Database.Cursor.execute(self, query, params)
    IntegrityError: recipe_04_todo.timestamp may not be NULL

If at this point some of these concepts like creating objects are feeling a bit rusty, now is a good time to read up on Python.

At this point nothing is visible in the browser, we haven't hooked anything up.

.. [#f1] http://docs.djangoproject.com/en/dev/ref/models/fields/
.. [#f2] We won't be doing this every time.
.. [#f3] http://docs.python.org/library/datetime.html#module-datetime