"""Serializers related to patient model."""
from django.utils import timezone
from rest_framework import serializers

from lab.models import Reports
from patient.models import Patient


class ReportSerializer(serializers.ModelSerializer):
    """Serializer for model report"""
    url = serializers.HyperlinkedIdentityField(view_name='report-detail')

    class Meta:
        """Defining the meta"""
        model = Reports
        fields = ['url']


class PatientSerializer(serializers.ModelSerializer):
    """Serializer for Patient"""
    url = serializers.HyperlinkedIdentityField(
        view_name='patient:patient-detail')
    admission_date = serializers.DateTimeField(default=timezone.now(),required =False)
    patient_reports = serializers.HyperlinkedIdentityField(many=True,
                                                           view_name='report-detail',
                                                           source='reports_set',required=False)

    class Meta:
        """Defining the meta for patient"""
        model = Patient
        fields = ['url', 'patient_name', 'admission_date',
                  'patient_contact', 'birth_date', 'gender',
                  'concerned_doctor', 'patient_reports']
