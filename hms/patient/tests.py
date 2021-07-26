"""
Test cases for various scenarios
"""
from django.test import Client, TestCase
from django.urls.base import reverse
from django.utils import timezone

from patient.models import Patient


def create_dummy_data():
    """Create a dummy patient object to be used for CRUD testing"""
    return Patient.objects.create (email='test@example.com',
                            password='patient1',
                            birth_date='1980-05-21',
                            patient_name='Test_Patient',
                            gender = 'M',
                            admission_date = timezone.now()
    )

class PatientModelTests(TestCase):
    """Test CRUD Operations for Patient"""
    def test_index_view(self):
        """Test for default Index view of all patients"""
        response = self.client.get(reverse('patient:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('patient/index.html')
    def test_detail_view(self):
        """Test for a detail view for a specific patient"""
        client = Client()
        test_patient = create_dummy_data()
        response = client.get(f'/patient/{test_patient.id}/')
        self.assertTemplateUsed('patient/detail.html')
        self.assertEqual(response.status_code, 200)
    def test_update_view(self):
        """Test for update view for a specific patient"""
        client = Client()
        test_patient = create_dummy_data()
        response = client.get(f'/patient/{test_patient.id}/patient_update_form')
        self.assertTemplateUsed('patient/patient_update_form.html')
        self.assertEqual(response.status_code, 200)
    def test_delete_view(self):
        """Test for delete view for a specific patient"""
        client = Client()
        test_patient = create_dummy_data()
        response = client.get(f'/patient/{test_patient.id}/delete')
        self.assertTemplateUsed('patient/patient_confirm_delete.html')
        self.assertEqual(response.status_code, 200)