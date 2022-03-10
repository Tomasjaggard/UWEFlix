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
    
class Address(models.Model):

    streetNumber = models.CharField(max_length=10)
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    post_code = models.CharField(max_length=7)

    class Meta:
        db_table = "Address"

    def __str__(self):
        template = '{0.streetNumber} {0.street}, {0.city}, {0.post_code}'
        return template.format(self) 

class ContactDetails(models.Model):

    # Regex Validator makes sure to accept a length of 11 made of digits.
    landline = models.CharField(max_length=11, validators=[RegexValidator(r'^\d{1,9}$')])
    mobile = models.CharField(max_length=11, validators=[RegexValidator(r'^\d{1,9}$')])
    email = models.EmailField(max_length=50)

    class Meta:
        db_table = "ContactDetails"

    def __str__(self):
        template = '{0.email}, {0.mobile}, {0.land_line}'
        return template.format(self) 

class Club(models.Model):
    name = models.CharField(max_length=30)
    address_fk = models.ForeignKey(Address, on_delete=models.CASCADE)
    contactDetails_fk = models.ForeignKey(ContactDetails, on_delete=models.CASCADE)

    class Meta:
        db_table = "Club"

    def __str__(self):
        template = '{0.name}, {0.address_fk}, {0.contactDetails_fk}'
        return template.format(self) 

class Representative(models.Model):
    
    firstName = models.CharField(max_length=30)
    lastName =  models.CharField(max_length=30)
    # TODO dob needs to be formatted - Format is set in forms
    dob = models.DateField(null=True)
    number = models.IntegerField(11, unique=True)
    password = models.CharField(max_length=20, blank=True, unique=True, default=uuid.uuid4)
    club_fk = models.ForeignKey(Club, on_delete=models.CASCADE, null='None')

    class Meta:
        db_table = "Representative"

class Account(models.Model):
    
    title = models.CharField(max_length=30)
    cardNumber = models.CharField(max_length=17)
    expiryDate = models.CharField(max_length=7)
    discountRate = models.IntegerField(11)
    club_fk = models.ForeignKey(Club, on_delete=models.CASCADE)

    class Meta:
        db_table = "Account"

class Transaction(models.Model):

    amount = models.FloatField(11)
    data = models.DateField(null=True)
    representative = models.ForeignKey(Representative, on_delete=models.CASCADE)
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





