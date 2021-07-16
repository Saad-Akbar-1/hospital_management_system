"""
Views for patient module
"""
from django.views import generic
from patient.models import  Patient # pylint: disable=import-error

class IndexView(generic.ListView):
    """Index View for all patients"""
    template_name = 'patient/index.html'
    context_object_name = 'latest_patient_list'

    def get_queryset(self):
        """Return the last five patients admitted."""
        return Patient.objects.order_by('-admission_date')[:5]

class DetailView(generic.DetailView):
    """Detail View for a particular Patient"""
    model = Patient
    template_name = 'patient/detail.html'
