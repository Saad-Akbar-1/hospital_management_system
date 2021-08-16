"""The Serializers to be used in REST API"""
from rest_framework import serializers

from doctor.models import Doctor
from lab.models import Reports
from patient.models import Patient


class PatientSerializer(serializers.ModelSerializer):
    """Serializer for model patient"""
    class Meta:
        """Defining meta for patient"""
        model = Patient
        fields = ['patient_name', 'admission_date', 'status']


class DoctorSerializer(serializers.ModelSerializer):
    """Serializer for model doctor"""
    class Meta:
        """Defining meta for doctor"""
        model = Doctor
        fields = ['fullname', 'specialisation', 'profilepic']


class ReportSerializer(serializers.ModelSerializer):
    """Serializer for model report"""
    url = serializers.HyperlinkedIdentityField(view_name='report-detail')
    Concerned_doctor = DoctorSerializer(
        read_only=True, source='concerned_doctor')
    Report = PatientSerializer(read_only=True, source='report')

    class Meta:
        """Defining meta for Reports which is displayed"""
        model = Reports
        fields = ['url', 'report', 'concerned_doctor',
                  'reporttype', 'Report', 'Concerned_doctor']


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     """Serializer for users so they can see the reports they made"""
#     reports = serializers.HyperlinkedRelatedField(
#         many=True, view_name='report-detail', read_only=True)

#     class Meta:
#         """Defining meta for user"""
#         model = User
#         fields = ['url', 'id', 'username', 'reports']
