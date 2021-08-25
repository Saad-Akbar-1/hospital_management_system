"""Test cases for REST API lab"""
from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from doctor.models import Doctor
from patient.models import Patient


class PatientTests(APITestCase):
    """CRUD Test on Patient"""

    def setUp(self):
        self.user = User.objects.create_user(
            username='test',
            email='test@email.com',
            password='test',
        )
        token, created = Token.objects.get_or_create(user=self.user)
        self.client = Client(HTTP_AUTHORIZATION='Token ' + token.key)

        doctor = Doctor.objects.create(
            username='testdoctor',
            password='testdoctor1',
            fullname='TestDoctor',
            specialisation="Cardiology",
            profilepic='black.png'
        )
        Patient.objects.create(
            birth_date='1980-05-21',
            patient_name='testpatient1',
            gender='M',
            admission_date=timezone.now(),
            concerned_doctor=doctor,
            status="A"
        )
        url = reverse('report-list')
        doctor = Doctor.objects.get()
        patient = Patient.objects.get()
        data = {'reporttype': 'CT', 'report': patient.id,
                'concerned_doctor': doctor.id}
        self.client.post(url, data)

    def test_create_patient(self):
        """
        Ensure we can create a new patient object.
        """
        url = reverse('patient:patient-list')
        data = {
            "birth_date": "1980-05-21",
            "patient_name": "testpatient2",
            "status": "A",
            "gender": "M",
            "patient_contact" : "+12342134523"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Patient.objects.count(), 2)

    def test_patient_detail_after_updating(self):
        """
        Ensure we can see details of object after updating
        """
        url = reverse('doctor-list')
        response = self.client.get(reverse(
            'patient:patient-detail', kwargs={'pk': Patient.objects.get(patient_name='testpatient1').id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Patient.objects.count(), 1)

    def test_delete_patient(self):
        """
        Ensure we can delete the object
        """
        response = self.client.delete(
            reverse('patient:patient-detail', kwargs={'pk': Patient.objects.get().id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Patient.objects.count(), 0)
