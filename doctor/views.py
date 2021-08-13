"""All of the doctor views"""
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from doctor.forms import SignUpForm
from doctor.models import Doctor
from lab.serializers import ReportSerializer


class IndexView(View):
    """List of all Doctors"""
    template_name = 'doctor/index.html'
    # context_object_name = 'doctor_list' needed in case of Generic.Listview

    def get_queryset(self):
        """Return the list of Doctors."""
        return Doctor.objects.all()

    def get(self, request):
        doctors = self.get_queryset()
        context = {'doctor_list': doctors}
        return render(request, 'doctor/index.html', context)


class DetailView(View):
    """Detail view for a single doctor object"""
    template_name = 'doctor/detail.html'

    def get(self, request, pk):
        """the get request that renders the doctor detail view"""
        doctor = Doctor.objects.get(id=pk)
        patients = doctor.patient_set.all()
        reports = doctor.reports_set.all()
        serializedreports = ReportSerializer(
            reports, many=True, context={'request': request})
        urls = [url['url'] for url in serializedreports.data]
        context = {'doctor': doctor, 'patients': patients,
                   'reports': zip(urls, reports)}
        return render(request, 'doctor/detail.html', context)


class UpdateDoctorView(View):
    """The base update doctor view"""

    def get(self, request, id=-1):
        """Return add new order form."""
        if id == -1:
            form = SignUpForm()
            return render(request, 'doctor/signup.html',
                          {'form': form, 'Text': 'Add a new Doctor'})
        doctor = get_object_or_404(Doctor, id=id)
        if doctor:
            form = SignUpForm(instance=doctor)
            return render(request, 'doctor/signup.html',
                          {'form': form, 'Text': 'Update Doctor'})

    def post(self, request, id):
        """Save order and redirect to order list."""
        doctor = get_object_or_404(Doctor, id=id)
        form = SignUpForm(request.POST, request.FILES, instance=doctor)
        if form.is_valid():
            new_doctor = form.save(commit=False)
            new_doctor.doctor = doctor
            new_doctor.save()
            return redirect('doctor:index')
        else:
            return render(request, 'doctor/signup.html', {'form': form, 'Text': 'Update Doctor'})


class AddDoctorView(View):
    """View for adding a doctor"""

    def get(self, request):
        """Return add new order form."""
        form = SignUpForm()
        return render(request, 'doctor/signup.html',
                      {'form': form, 'Text': 'Add a new Doctor'})

    def post(self, request):
        """Save order and redirect to order list."""
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            new_doctor = form.save()
            new_doctor.save()
            return redirect('doctor:index')
        else:
            return render(request, 'doctor/signup.html', {'form': form, 'Text': 'Add a new Doctor'})


class DeleteDoctor(View):
    """The delete view"""

    def get(self, request, id):
        """request to delete"""
        doctor = get_object_or_404(Doctor, id=id)
        doctor.delete()
        return redirect('doctor:index')
