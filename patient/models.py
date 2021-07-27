"""
This is where schema (and models) are defined.
"""
import datetime

from django.contrib import admin
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _
from phonenumber_field.modelfields import PhoneNumberField


class Patient(AbstractUser):
    '''Basic Patient model, stores common info of patients'''
    username = None
    email = models.EmailField(_('email address'), unique=True,default="someone@example.com")
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    password = models.CharField(max_length=200, default='patient1')
    birth_date = models.DateField(null=True, blank=True)
    patient_name = models.CharField(max_length=200)
    admission_date = models.DateTimeField('Date of Admission')
    patient_contact = PhoneNumberField(max_length=15)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,default='M')
    def __str__(self):
        '''Returns the name of current patient'''
        return str(self.patient_name)

    @admin.display(
        boolean=True,
        ordering='admission_date',
        description='Admitted recently?',
    )
    def is_admitted_recently(self):
        '''Is the patient admitted in last 24 hours.'''
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.admission_date <= now
