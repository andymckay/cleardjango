from django.test import TestCase
from django.db import IntegrityError

from models import Todo

from datetime import datetime

class TodoTest(TestCase):
    def testTodo(self):
        assert Todo.objects.count() == 0

    def testAddTodo(self):
        todo = Todo()
        todo.text = "Get some milk"
        todo.timestamp = datetime.now()
        todo.save()

    def testAddTodoNoTimestamp(self):
        todo = Todo()
        todo.text = "Get some milk"
        self.assertRaises(IntegrityError, todo.save)
