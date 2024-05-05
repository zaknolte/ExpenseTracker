from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Sum

# Create your models here.
CATEGORY_CHOICES = [
    ("Food","Food"),
    ("Travel","Travel"),
    ("Shopping","Shopping"),
    ("Necessities","Necessities"),
    ("Entertainment","Entertainment"),
    ("Other","Other")
]

TRANSACTION_CHOICES = [
    ("Expense","Expense"),
    ("Income","Income")
]

PROFESSION_CHOICES =[
    ("Employee","Employee"),
    ("Business","Business"),
    ("Student","Student"),
    ("Other","Other")
]


class Transactions(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10 , choices=TRANSACTION_CHOICES)
    amount = models.BigIntegerField()
    date = models.DateField(default=now)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES , default='Food')

    class Meta:
        db_table:'addmoney'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profession = models.CharField(max_length=10, choices=PROFESSION_CHOICES)
    savings = models.IntegerField( null=True, blank=True)
    income = models.BigIntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return self.user.username
    