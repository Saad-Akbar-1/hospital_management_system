"""
This is where schema (and models) are defined.
"""
import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin
from phonenumber_field.modelfields import PhoneNumberField

class Patient(models.Model):
    '''Basic Patient model, stores common info of patients'''
    patient_name = models.CharField(max_length=200)
    admission_date = models.DateTimeField('Date of Admission')
    patient_email = models.EmailField(max_length=200)
    patient_contact = PhoneNumberField(max_length=15)
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
