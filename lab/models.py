"""Defining models for lab here"""
from django.db import models
from django.db.models.deletion import CASCADE

from doctor.models import Doctor
from patient.models import Patient


class Reports(models.Model):
    """The report of a particular patient prescribed by a doctor"""
  

    report = models.ForeignKey(
        Patient, on_delete=CASCADE,
        help_text="Select the relevant Patient",
        blank=True, null=True
    )
    REPORT_CHOICES = (
        ('R', 'Radiology Report'),
        ('B', 'Blood Report'),
        ('CT', 'CT Scan')
    )
    reporttype = models.CharField(
        choices=REPORT_CHOICES, default='B', max_length=2)
    concerned_doctor = models.ForeignKey(Doctor, on_delete=CASCADE,
                                         help_text="The Prescribing Doctor",
                                         blank=True, null=True)

    def __str__(self):
        return str(self.report)
