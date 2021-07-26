"""
Views for patient module
"""
from django.urls.base import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse
from patient.models import  Patient 
from patient.forms import SignUpForm

def signup_view(request):
    """The sign up view for the Patient Mdoel"""
    form = SignUpForm(request.POST)
    if form.is_valid():
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
                    gender = genderchoice
                    )
        patient.save()
        return redirect(str(patient.id)+'/detail')
    form = SignUpForm
    return render(request, 'patient/signup.html', {'form': form})



class IndexView(generic.ListView):
    """Index View for all patients"""
    template_name = 'patient/index.html'
    context_object_name = 'latest_patient_list'


    def get_queryset(self):
        """Return the last five patients admitted."""
        return Patient.objects.order_by('-admission_date')

class DetailView(generic.DetailView):
    """Detail View for a particular Patient"""
    model = Patient
    template_name = 'patient/detail.html'

class PatientUpdateView(UpdateView):
    """The update view for the Patient model"""
    model = Patient
    fields = ['patient_name','email','patient_contact','birth_date','gender']
    template_name_suffix = '_update_form'
    def get_success_url(self) -> str:
        return reverse('patient:index')

class PatientDeleteView(DeleteView):
    DeleteView.model = Patient
    template_name = "patient/patient_confirm_delete.html"  
    
    def get_success_url(self) -> str:
        return reverse_lazy('patient:index')
    

    
