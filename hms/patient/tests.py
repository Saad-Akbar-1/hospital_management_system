"""
Test cases for various scenarios
"""
import datetime

from django.test import TestCase
from django.utils import timezone
from patient.models import Patient


class PatientModelTests(TestCase):
    def was_admitted_recently_with_future_admission_date(self):
        '''
        Tests to see a patient who's scheduled to be admitted in the 
        future does not show up in admitted recently list
        '''
        admission_time = timezone.now() + datetime.timedelta(days=30)
        future_patient = Patient(patient_name="FuturePatient1",
                                admission_date=admission_time,
                                patient_email="someone121@example.com",
                                patient_contact="+1123455653421"
                                )
        self.assertIs(future_patient.is_admitted_recently(), False)
