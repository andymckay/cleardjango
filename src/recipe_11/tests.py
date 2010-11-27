from django.test import TestCase                
from django.test.client import Client

class tests(TestCase):
    def testFunction(self):
        clt = Client()
        res = clt.get("/hello-function/")
        assert res.status_code == 200
        assert res.content == 'Hello world!'
        
    def testClass(self):
        clt = Client()
        res = clt.get("/hello-class/")
        assert res.status_code == 200
        assert res.content == 'Hello world!'