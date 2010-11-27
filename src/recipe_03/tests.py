from django.test import TestCase
from models import Todo

class TodoTest(TestCase):
    def testTodo(self):
        assert Todo.objects.count() == 0