from django.test import TestCase, Client             
from models import BankAccount, Log
from decimal import Decimal
from django.contrib.auth.models import User

class tests(TestCase):
    def testReadOnly(self):
        bank = BankAccount()
        bank.number = "1234567890"
        bank.amount = Decimal("100.00")
        bank.save()
        
        logs = Log.objects.all()
    
    def testClient(self):
        user = User()
        user.username="admin"
        user.set_password("admin")
        user.is_active = True
        user.is_superuser = True
        user.save()
        
        clt = Client()
        clt.login(username="admin", password="admin")
        res = clt.get("/update/")
        assert res.status_code == 200, "Got %s, %s" % (res.status_code, res.items())
        logs = Log.objects.all()
