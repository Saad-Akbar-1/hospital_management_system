from django.test import Client, TestCase
from django.urls.base import reverse

from doctor.models import Doctor


def create_dummy_data():
    """Create a dummy Doctor object to be used for CRUD testing"""
    return Doctor.objects.create(username='testdoctor',
                                 password='testdoctor1',
                                 fullname='TestDoctor',
                                 )


class PatientModelTests(TestCase):
    """Test CRUD Operations for Doctor"""

    def test_index_view(self):
        """Test for default Index view of all Doctor"""
        response = self.client.get(reverse('doctor:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('doctor/index.html')

    def test_detail_view(self):
        """Test for a detail view for a specific Doctor"""
        client = Client()
        test_doctor = create_dummy_data()
        response = client.get(f'/doctor/{test_doctor.id}/')
        self.assertTemplateUsed('doctor/detail.html')
        self.assertEqual(response.status_code, 200)

    def test_update_view(self):
        """Test for update view for a specific Doctor"""
        client = Client()
        test_doctor = create_dummy_data()
        response = client.get(
            f'/doctor/{test_doctor.id}/update')
        self.assertTemplateUsed('doctor/signup.html')
        self.assertEqual(response.status_code, 200)

    def test_delete_view(self):
        """Test for delete view for a specific Doctor"""
        client = Client()
        test_doctor = create_dummy_data()
        response = client.get(f'/doctor/{test_doctor.id}/delete', follow=True)

        self.assertTemplateUsed('doctor/delete.html')
        self.assertEqual(response.status_code, 200)

    def test_signup_view(self):
        """Test for signup view for a specific Doctor"""
        client = Client()
        response = client.get('/doctor/signup', follow=True)
        self.assertTemplateUsed('doctor/signup.html')
        self.assertEqual(response.status_code, 200)
