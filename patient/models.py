"""
This is where schema (and models) are defined.
"""
import datetime

from django.contrib import admin
from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

from doctor.models import Doctor


class Patient(models.Model):
    '''Basic Patient model, stores common info of patients'''
    birth_date = models.DateField(null=True, blank=True)
    patient_name = models.CharField(max_length=200)
    admission_date = models.DateTimeField('Date of Admission')
    patient_contact = PhoneNumberField(max_length=15)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    concerned_doctor = models.ForeignKey(
        Doctor, on_delete=CASCADE, help_text="Assign the Doctor", blank=True, null=True)
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, default='M')
    ADMITTED, IN_PROGRESS, UNDER_OPERATION, DISCHARGED = 'A', 'I', 'U', 'D'
    status_choices = [(ADMITTED, 'Admitted'), (IN_PROGRESS, 'In Progress'),
                      (UNDER_OPERATION, 'Under Operation'), (DISCHARGED, 'Discharged')]

    status = models.CharField(
        max_length=1,
        choices=status_choices,
        default=ADMITTED
    )

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
