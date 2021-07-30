"""
Views for patient module
"""
from django.shortcuts import redirect
from django.urls import reverse
from django.urls.base import reverse_lazy
from django.utils import timezone
from django.views import generic
from django.views.generic.edit import DeleteView, UpdateView

from patient.forms import SignUpForm
from patient.models import Patient


class SignupView(generic.FormView):
    '''The signup view that uses a Signup form class as its form'''
    template_name = 'patient/signup.html'
    form_class = SignUpForm

    def form_valid(self, form):
        name = form.cleaned_data.get('patient_name')
        contact = form.cleaned_data.get('patient_contact')
        emailid = form.cleaned_data.get('patient_email')
        dob = form.cleaned_data.get('birth_date')
        genderchoice = form.cleaned_data.get('gender')
        date = timezone.now()
        patient = Patient(patient_name=name,
                          admission_date=date,
                          email=emailid,
                          patient_contact=contact,
                          birth_date=dob,
                          gender=genderchoice
                          )
        patient.save()
        return redirect(str(patient.id)+'/detail')


class IndexView(generic.ListView):
    """Index View for all patients"""
    template_name = 'patient/index.html'
    context_object_name = 'latest_patient_list'

    def get_queryset(self):
        """Return the patients admitted order by recent admission date."""
        return Patient.objects.order_by('-admission_date')


class DetailView(generic.DetailView):
    """Detail View for a particular Patient"""
    model = Patient
    template_name = 'patient/detail.html'


class PatientUpdateView(UpdateView):
    """The update view for the Patient model"""
    model = Patient
    fields = ['patient_name', 'email', 'patient_contact',
              'birth_date', 'gender', 'concerned_doctor', 'status']
    template_name_suffix = '_update_form'

    def get_success_url(self) -> str:
        return reverse('patient:index')


class PatientDeleteView(DeleteView):
    """The Delete view for patient model."""
    DeleteView.model = Patient
    template_name = "patient/patient_confirm_delete.html"

    def get_success_url(self) -> str:
        return reverse_lazy('patient:index')
