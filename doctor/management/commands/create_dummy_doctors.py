"""Create dummy doctors to populate database"""
from django.core.management.base import BaseCommand

from doctor.models import Doctor


class Command(BaseCommand):
    """Create dummy doctors command class."""

    help = "Create dummy doctors for testing purposes."

    def add_arguments(self, parser):
        """specify how many doctors to create"""
        parser.add_argument(
            '--total', type=int, help='Indicates the number of doctors to be created.', default=8,
        )

    def handle(self, *args, **kwargs):
        """Create 'total' dummy doctors in database."""
        num_doctors = kwargs['total']
        if num_doctors < 1:
            self.stdout.write('Can not create less than 1 doctors.')

        else:
            dummy_doctor_list = []
            for i in range(num_doctors):
                doctor = Doctor(**{
                    'username': "DummyDoctor"+str(i),
                    'password': "Password"+str(i),
                    'fullname': 'Dummy Doctor'+str(i),
                    'specialisation': "General",
                })
                dummy_doctor_list.append(doctor)

            Doctor.objects.bulk_create(dummy_doctor_list)

            self.stdout.write('Dummy doctors created!')
