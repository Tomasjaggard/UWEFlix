import email
from operator import mod
from pyexpat import model
from statistics import mode
from time import time
from xml.dom.pulldom import START_DOCUMENT
from django.db import models
from django.forms import CharField, DateField, FloatField, IntegerField
from django.utils import timezone
import uuid
import datetime
from django.core.validators import RegexValidator

"""
Migrate DB with following commands:
python manage.py makemigrations
python manage.py migrate
"""

"""
    Student Club and Representative Models includes Transaction
"""
    
"""class Address(models.Model):

    streetNumber = models.CharField(max_length=10)
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    post_code = models.CharField(max_length=7)

    class Meta:
        db_table = "Address"

    def __str__(self):
        template = '{0.streetNumber} {0.street}, {0.city}, {0.post_code}'
        return template.format(self) 
    class Meta:
        db_table = "ContactDetails"

    def __str__(self):
        template = '{0.email}, {0.mobile}, {0.landline}'
        return template.format(self) 
"""

class Representative(models.Model):
    
    firstName = models.CharField(max_length=30)
    lastName =  models.CharField(max_length=30)
    # TODO dob needs to be formatted - Format is set in forms
    dob = models.DateField(null=True)
    number = models.IntegerField('Number', unique=True)
    password = models.CharField(max_length=36, blank=True, unique=True, default=uuid.uuid4)
    #club = models.ForeignKey(Club, on_delete=models.CASCADE, null='None')

    class Meta:
        db_table = "Representative"

class Club(models.Model):
    name = models.CharField(max_length=30)
    streetNumber = models.CharField(max_length=10)
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    post_code = models.CharField(max_length=7)
    landline = models.IntegerField('landline')
    mobile = models.IntegerField('Mobile')
    email = models.EmailField(max_length=50)
    rep = models.ForeignKey(Representative, on_delete=models.CASCADE)
    #address_fk = models.ForeignKey(Address, on_delete=models.CASCADE, null=False)
    #contactDetails_fk = models.ForeignKey(ContactDetails, on_delete=models.CASCADE, null=False)

    class Meta:
        db_table = "Club"
        
    def __str__(self):
        template = '{0.name}'
        return template.format(self) 

class Account(models.Model):
    
    title = models.CharField(max_length=30)
    cardNumber = models.CharField(max_length=17)
    expiryDate = models.CharField(max_length=7)
    discountRate = models.IntegerField(11)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)

    class Meta:
        db_table = "Account"

class Transaction(models.Model):

    amount = models.FloatField(11)
    data = models.DateField(null=True)
    #representative = models.ForeignKey(Representative, on_delete=models.CASCADE)
    account_fk = models.ForeignKey(Account, on_delete=models.CASCADE)

    class Meta:
        db_table = "Transaction"



"""             
    Cinema Models including Cinema, Screen, Film and Showing.
"""

class Cinema(models.Model):

    # Default to False intially
    socialDist = models.BooleanField(False)

    class Meta:
        db_table = "Cinema"

    def __str__(self):
        template = 'UWEFlix'
        return template.format(self) 

class Screen(models.Model):

    screenNumber = models.IntegerField("Screen Number")
    capacity = models.IntegerField("Capacity")
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)

    class Meta:
        db_table = "Screen"

    def __str__(self):
        template = '{0.screenNumber}'
        return template.format(self) 

class Film(models.Model):

    title = models.CharField(max_length=30)
    age = models.IntegerField("Age Rating")
    duration = models.FloatField("Duration in Minutes")
    description = models.CharField(max_length=200)

    class Meta:
        db_table = "Film"

    def __str__(self):
        template = '{0.title}'
        return template.format(self) 
    
class Showing(models.Model):

    # TODO formatting needed - no longer null = True
    date = models.DateField(("Date"), default=datetime.date.today)
    time = models.TimeField("Time")
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "Showing"

    def __str__(self):
        template = '{0.date}'
        return template.format(self) 

"""
        TODO    
"""

class Ticket(models.Model):
    
    studentPrice = models.FloatField(11)
    childPrice = models.FloatField(11)
    adultPrice = models.FloatField(11)

    class Meta:
        db_table = "Ticket"


class Booking(models.Model):
    
    studentQuantity = models.IntegerField(11)
    childQuantity = models.IntegerField(11)
    adultQuantity= models.IntegerField(11)

    class Meta:
        db_table = "Booking"





