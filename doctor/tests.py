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


class DoctorTest(APITestCase):
    """CRUD Test on Doctor"""

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
        )
        Patient.objects.create(
            birth_date='1980-05-21',
            patient_name='testpatient',
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

    def test_create_doctor(self):
        """
        Ensure we can create a new doctor object.
        """
        url = reverse('doctor-list')
        data = {
            "username": "testdoctor",
            "password": "testdoctor1",
            "fullname": "TestDoctor",
            "specialisation" : "Cardiology"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Doctor.objects.count(), 2)

    def test_doctor_detail_after_updating(self):
        """
        Ensure we can see details of object after updating
        """
        url = reverse('doctor-list')
        data = {
            'username': 'testdoctor2',
            'password': 'testdoctor1',
            'fullname': 'TestDoctor',
            'specialisation': "Cardiology",
            'profilepic': 'black.png'
        }
        response = self.client.post(url, data)
        response = self.client.get(reverse(
            'doctor-detail', kwargs={'pk': Doctor.objects.get(username='testdoctor').id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Doctor.objects.count(), 1)

    def test_delete_doctor(self):
        """
        Ensure we can delete the object
        """
        response = self.client.delete(
            reverse('doctor-detail', kwargs={'pk': Doctor.objects.get().id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Doctor.objects.count(), 0)
