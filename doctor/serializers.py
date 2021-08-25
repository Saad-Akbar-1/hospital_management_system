"""The Custom Serializers for the Doctor Model."""

from rest_framework import serializers
from rest_framework.relations import HyperlinkedIdentityField

from doctor.models import Doctor
from patient.models import Patient


class PatientSerializer(serializers.ModelSerializer):
    """Serializer for model patient"""
    class Meta:
        """Defining meta for patient"""
        model = Patient
        fields = ['patient_name', 'admission_date', 'gender', 'status']


class DoctorSerializer(serializers.ModelSerializer):
    """Serializer for model doctor"""
    url = serializers.HyperlinkedIdentityField(view_name='doctor-detail')
    assigned_patients = HyperlinkedIdentityField(
        many=True, source='patient_set', view_name='patient:patient-detail',required=False)

    class Meta:
        """Defining meta for doctor"""
        model = Doctor
        fields = ['url', 'fullname', 'specialisation',
                  'profilepic', 'assigned_patients']
