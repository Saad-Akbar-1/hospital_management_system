"""The main views for REST framweork"""
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from lab.models import Reports
from lab.serializers import ReportSerializer


@api_view(['GET'])
def api_root(request, format=None):
    """The main index"""
    return Response({
        'reports': reverse('report-list', request=request, format=format)

    })


class ReportList(generics.ListCreateAPIView):
    """ListView for reports"""
    queryset = Reports.objects.all()
    serializer_class = ReportSerializer
  


class ReportDetail(generics.RetrieveUpdateDestroyAPIView):
    """Detail View for reports."""
    queryset = Reports.objects.all()
    serializer_class = ReportSerializer
   