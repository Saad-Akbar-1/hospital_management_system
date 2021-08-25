"""
Default index views to patient and doctor
"""
from django.shortcuts import render
from django.views import View
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    """The main index"""
    return Response({
        'Reports': reverse('report-list', request=request, format=format),
        'Doctors': reverse('doctor-list', request=request,format=format),
        'Patients': reverse('patient:patient-list', request=request,format=format)

    })


class MainIndex(View):
    """Basic index view"""
    template_name = 'hms/index.html'

    def get(self, request):
        """Return the index page"""
        return render(request, 'hms/index.html')
