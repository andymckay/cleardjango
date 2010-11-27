from django.test import TestCase, Client

class test(TestCase):
    def testHello(self):
        client = Client()
        response = client.get("/")
        assert response.content == "Hello, world!"