from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase
from lab.models import Reports
from lab.views import ReportDetail


class ReportsTests(APITestCase):
    def test_create_report(self):
        """
        Ensure we can create a new report object.
        """
        url = reverse('report-list')
        data = {'reporttype': 'CT'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Reports.objects.count(), 1)
        response = self.client.get(reverse('report-detail',kwargs={'pk':1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        


    def test_detail_report(self):
        """
        Ensure we can see details of object
        """
        url = reverse('report-list')
        data = {'reporttype': 'CT'}
        response = self.client.post(url, data)
        response = self.client.get(reverse('report-detail',kwargs={'pk':2}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
