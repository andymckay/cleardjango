from django.test import TestCase
from django.core.paginator import Paginator

from models import Todo

class TodoTest(TestCase):
    def setUp(self):
        for x in range(0, 23):
            todo = Todo()
            todo.text = "Item: %s" % x
            todo.save()
            
    def testPage(self):
        objects = Todo.objects.all()
        front_page = objects[:7]
        p = Paginator(objects[7:], 10)
        assert p.page_range == 2
        
        