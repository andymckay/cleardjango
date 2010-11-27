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
        todo.save()

    def testAlterTodo(self):
        todo = Todo()
        todo.text = "Get some milk"
        todo.timestamp = datetime.now()
        todo.save()
        
        assert not todo.completed
        todo.completed = True
        todo.save()
        
        assert todo.completed
    
    def testAlterAndQueryTodo(self):
        todo = Todo()
        todo.text = "Get some milk"
        todo.timestamp = datetime.now()
        todo.save()
        
        id = todo.id
        
        assert Todo.objects.filter(completed=False).count() == 1
        
        todo = Todo.objects.get(id=id)
        todo.completed = True
        todo.save()
        
        assert Todo.objects.filter(completed=False).count() == 0