from django.db.models.signals import post_save
from django.contrib.auth.models import Group, User
from .models import *


def customer_profile(sender, instance, created, **kwargs):
    if created:
        group, _ = Group.objects.get_or_create(name='customer')
        instance.groups.add(group)
        Customer.objects.create(user=instance, name=instance.username)
        print('Customer profile created!')

post_save.connect(customer_profile, sender=User)


def deposit(sender, instance, created, **kwargs):
    if created:
        group, _ = Group.objects.get_or_create(name='deposit')
        instance.groups.add(group)
        Deposit.objects.create(user=instance, name=instance.username)
        print('Deposit profile created!')

post_save.connect(deposit, sender=User)


def profile_profile(sender, instance, created, **kwargs):
    if created:
        group, _ = Group.objects.get_or_create(name='profile')
        instance.groups.add(group)
        Profile.objects.create(user=instance, name=instance.username)
        print('Profile created!')

post_save.connect(profile_profile, sender=User)


def account(sender, instance, created, **kwargs):
    if created:
        group, _ = Group.objects.get_or_create(name='account')
        instance.groups.add(group)
        Account.objects.create(user=instance, name=instance.username)
        print('Account profile created!')

post_save.connect(account, sender=User)


def transaction(sender, instance, created, **kwargs):
    if created:
        group, _ = Group.objects.get_or_create(name='transaction')
        instance.groups.add(group)
        Transaction.objects.create(user=instance, name=instance.username)
        print('Transaction profile created!')

post_save.connect(transaction, sender=User)


def transactionone(sender, instance, created, **kwargs):
    if created:
        group, _ = Group.objects.get_or_create(name='transactionone')
        instance.groups.add(group)
        Transactionone.objects.create(user=instance, name=instance.username)
        print('Transaction One profile created!')

post_save.connect(transactionone, sender=User)


def transactiontwo(sender, instance, created, **kwargs):
    if created:
        group, _ = Group.objects.get_or_create(name='transactiontwo')
        instance.groups.add(group)
        Transactiontwo.objects.create(user=instance, name=instance.username)
        print('Transaction Two profile created!')

post_save.connect(transactiontwo, sender=User)


def transactionthree(sender, instance, created, **kwargs):
    if created:
        group, _ = Group.objects.get_or_create(name='transactionthree')
        instance.groups.add(group)
        Transactionthree.objects.create(user=instance, name=instance.username)
        print('Transaction Three profile created!')

post_save.connect(transactionthree, sender=User)


def wallet(sender, instance, created, **kwargs):
    if created:
        group, _ = Group.objects.get_or_create(name='wallet')
        instance.groups.add(group)
        Wallet.objects.create(user=instance, name=instance.username)
        print('Wallet profile created!')

post_save.connect(wallet, sender=User)


def pin(sender, instance, created, **kwargs):
    if created:
        group, _ = Group.objects.get_or_create(name='pin')
        instance.groups.add(group)
        Pin.objects.create(user=instance, name=instance.username)
        print('Pin profile created!')

post_save.connect(pin, sender=User)
