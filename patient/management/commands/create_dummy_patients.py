"""Create dummy doctors to populate database"""
from django.core.management.base import BaseCommand
from django.utils import timezone

from doctor.models import Doctor
from patient.models import Patient


class Command(BaseCommand):
    """Create dummy patients command class."""

    help = "Create dummy patients for testing purposes."

    def add_arguments(self, parser):
        """specify how many patients to create"""
        parser.add_argument(
            '--total', type=int, help='Indicates the number of patients to be created.', default=8,
        )

    def handle(self, *args, **kwargs):
        """Create 'total' dummy patients in database."""
        num_doctors = kwargs['total']
        if num_doctors < 1:
            self.stdout.write('Can not create less than 1 patients.')

        else:
            dummy_patient_list = []
            for i in range(num_doctors):
                patient = Patient(**{
                    'birth_date': "1980-05-21",
                    'patient_name': "dummypatient"+str(i),
                    'admission_date' : timezone.now(),
                    'gender': 'M',
                    'status': "A",
                    'concerned_doctor' : Doctor.objects.get(username="DummyDoctor"+str(i))
                })
                dummy_patient_list.append(patient)

            Patient.objects.bulk_create(dummy_patient_list)

            self.stdout.write('Dummy patients created!')
