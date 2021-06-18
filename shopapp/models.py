from django.db import models
from .models import *

# Create your models here.
class Dealer(models.Model):
    dname = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    phone_no = models.BigIntegerField(unique=True)
    email = models.CharField(max_length=50)

    class Meta:
        db_table = 'dealerinfo'

    def __str__(self):
        return self.email

class Employee(models.Model):
    emp_id = models.IntegerField(unique=True)
    fname = models.CharField(max_length=40)
    lname = models.CharField(max_length=40)
    address = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    salary = models.CharField(max_length=40)
    phone_no= models.BigIntegerField(unique=True)

    class Meta:
        db_table = 'employeeinfo'

    def __str__(self):
        return self.email

class Customer(models.Model):
    cid = models.IntegerField(unique=True)
    fname = models.CharField(max_length=40)
    lname = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    email = models.CharField(max_length=100)
    phone_no = models.BigIntegerField(unique=True)

    class Meta:
        db_table = 'customerinfo'

    def __str__(self):
        return self.email

class Medicine(models.Model):
    m_id = models.IntegerField(unique=True)
    mname = models.CharField(max_length=50)
    dname = models.CharField(max_length=50)
    desc = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    stock = models.IntegerField()
    expiry_date = models.DateField()

    class Meta:
        db_table = 'medicineinfo'

    def __str__(self):
        return self.mname
class Purchase(models.Model):
    p_id = models.IntegerField(unique=True)
    mname = models.CharField(max_length=30)
    dname = models.CharField(max_length=30)
    desc = models.CharField(max_length=100)
    phone_no = models.BigIntegerField()
    price = models.BigIntegerField()
    stock = models.BigIntegerField()
    total = models.DecimalField(max_digits=10,decimal_places=2)

    class Meta:
        db_table = 'purchaseinfo'

    def __str__(self):
        return self.pname

class Custpurchase(models.Model):
    p_id = models.IntegerField(unique=True)
    fname = models.CharField(max_length=40)
    lname = models.CharField(max_length=40)
    mname = models.CharField(max_length=30)
    desc = models.CharField(max_length=100)
    phone_no = models.BigIntegerField()
    price = models.BigIntegerField()
    quantity = models.IntegerField()
    total = models.DecimalField(max_digits=10,decimal_places=2)

    class Meta:
        db_table = 'custpurchaseinfo'

    def __str__(self):
        return self.pname
