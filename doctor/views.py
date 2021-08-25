"""All of the doctor views"""
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from doctor.models import Doctor
from doctor.serializers import DoctorSerializer
from lab.views import TokenLoginRequiredMixin


class DoctorList(TokenLoginRequiredMixin, generics.ListCreateAPIView):
    """List of Doctors REST API"""
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class DetailDoctor(TokenLoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    """Detail of a particular Doctor REST API"""
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
