Recipe 4: A first model, with fields
--------------------------------------------------
   
.. topic:: Recipe 4
    
    Run: ``python tools/configure.py -s 4`` to install and run this recipe.

Let's add some fields to the last recipe to make it more interesting. A field is the definition of the column in the database. So let's give our *Todo* model the following fields:

* *text* some details about the todo item eg: "Go get milk"

* *completed* a Yes/No flag to see if the todo has been completed

* *timestamp* a timestamp for when the model has been completed

This would change the model to look like the following:

.. literalinclude:: ../src/recipe_04/models.py
   :linenos:
   :lines: 1-6

There's lots of fields available to you and the full reference of them can be found online [#f1]_. It would be fantastically boring to relist them all here, so I won't bother. But basically you can see we have *CharField*, a *BooleanField* and a *DateTimeField* which all correspond to the data.

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

So we've got a model, how do we create a record in the database of this? It's pretty simple, create an instance of the class, assign values to the fields and then call the save method on the class. For example:

.. code-block:: python
    :linenos:

    from datetime import datetime

    todo = Todo()
    todo.text = "Get some milk"
    todo.timestamp = datetime.now()
    todo.save()
   
You'll see that the assignment of values to the object matches the fields. If the field is called "text" then you assign to text (as per line 2). At the end calling save performs all the necessary SQL inserts into the database.

In this model, we've set a default value for *completed* to be False. By default when you create a todo item, it won't be completed. So in the above piece of code, we didn't bother setting the value for *completed*. But we did set one for *timestamp*, what happens if you don't for example:

.. code-block:: python
    :linenos:
    
    todo = Todo()
    todo.text = "Get some milk"
    todo.save()

You'll get an error::
    
      File "/usr/lib/python2.5/site-packages/django/db/backends/sqlite3/base.py", line 193, in execute
        return Database.Cursor.execute(self, query, params)
    IntegrityError: recipe_04_todo.timestamp may not be NULL

If at this point some of these concepts like creating objects are feeling a bit rusty, now is a good time to read up on Python. Django has done it's best to be like Python as much as it can so it really pays to learn that. Besides I'm not going to spell it out much since a) I'm lazy and b) this isn't a book about Python.

.. [#f1] http://docs.djangoproject.com/en/dev/ref/models/fields/
.. [#f2] Last time I'll do this for a while, you've got the idea now?
