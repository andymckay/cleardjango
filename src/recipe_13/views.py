from django.test import TestCase                
from models import BankAccount, Log
from django.contrib.auth.decorators import login_required
from decimal import Decimal
from django.http import HttpResponse


@login_required
def update(request):
    bank = BankAccount()
    bank.number = "1234567891"
    bank.amount = Decimal("100.00")
    bank.save()
    return HttpResponse("hello")