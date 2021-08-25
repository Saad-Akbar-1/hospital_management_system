"""
Views for patient module
"""


from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from lab.views import TokenLoginRequiredMixin
from patient.models import Patient
from patient.serializers import PatientSerializer


class PatientList(TokenLoginRequiredMixin, generics.ListCreateAPIView):
    """List of all patients."""
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class PatientDetail(TokenLoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    """Details of the particular patient."""
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
