"""Test cases for REST API lab"""
from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from doctor.models import Doctor
from lab.models import Reports
from patient.models import Patient


class ReportsTests(APITestCase):
    """CRUD Test on Reports"""

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

    def test_create_report(self):
        """
        Ensure we can create a new report object.
        """
        url = reverse('report-list')
        doctor = Doctor.objects.get()
        patient = Patient.objects.get()
        data = {'reporttype': 'B', 'report': patient.id,
                'concerned_doctor': doctor.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Reports.objects.count(), 2)

    def test_detail_report_after_updating(self):
        """
        Ensure we can see details of object after updating
        """
        url = reverse('report-list')
        data = {}
        data['reporttype'] = 'CT'
        response = self.client.put(url, data)
        response = self.client.get(
            reverse('report-detail', kwargs={'pk': Reports.objects.get().id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Reports.objects.count(), 1)

    def test_delete_report(self):
        """
        Ensure we can delete the object
        """
        response = self.client.delete(
            reverse('report-detail', kwargs={'pk': Reports.objects.get().id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Reports.objects.count(), 0)
