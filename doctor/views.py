from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from doctor.forms import SignUpForm
from doctor.models import Doctor


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


def formview(request):
    context = {}
    if request.method == "POST":
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get("username")
            passw = form.cleaned_data.get("password")
            full_name = form.cleaned_data.get("fullname")
            img = form.cleaned_data.get("profilepic")
            doctor = Doctor.objects.create(
                username=name,
                password=passw,
                fullname=full_name,
                profilepic=img
            )
            doctor.save()
            return redirect(str(doctor.id)+'/detail')
    else:
        form = SignUpForm()
    context['form'] = form
    return render(request, "doctor/signup.html", context)


class DetailView(View):
    template_name = 'doctor/detail.html'

    def get(self, request, pk):
        doctor = Doctor.objects.get(id=pk)
        context = {'doctor': doctor}
        return render(request, 'doctor/detail.html', context)


class UpdateDoctorView(View):
    def get(self, request, id):
        """Return add new order form."""
        doctor = get_object_or_404(Doctor, id=id)
        form = SignUpForm()
        return render(request, 'doctor/signup.html',
                      {'form': form})

    def post(self, request, id):
        """Save order and redirect to order list."""
        form = SignUpForm(request.POST, request.FILES)
        doctor = get_object_or_404(Doctor, id=id)
        if form.is_valid():
            new_doctor = form.save(commit=False)
            new_doctor.doctor = doctor
            new_doctor.save()
            return redirect('doctor:index')
        else:
            return render(request, 'doctor/signup.html', {'form': form})


class DeleteDoctor(View):
    def get(self, request, id):
        doctor = get_object_or_404(Doctor, id=id)
        doctor.delete()
        return redirect('doctor:index')
