"""Create dummy doctors to populate database"""
from django.core.management.base import BaseCommand
from django.utils import timezone

from doctor.models import Doctor
from lab.models import Reports
from patient.models import Patient


class Command(BaseCommand):
    """Create dummy report class."""

    help = "Create dummy reports for testing purposes."

    def add_arguments(self, parser):
        """specify how many reports to create"""
        parser.add_argument(
            '--total', type=int, help='Indicates the number of reports to be created.', default=8,
        )

    def handle(self, *args, **kwargs):
        """Create 'total' dummy reports in database."""
        num_reports = kwargs['total']
        if num_reports < 1:
            self.stdout.write('Can not create less than 1 reports.')

        else:
            dummy_report_list = []
            for i in range(num_reports):
                report = Reports(**{
                    'reporttype': "CT",
                    'report': Patient.objects.get(patient_name="dummypatient"+str(i)),
                    'concerned_doctor': Doctor.objects.get(username="DummyDoctor"+str(i))
                })
                dummy_report_list.append(report)

            Reports.objects.bulk_create(dummy_report_list)

            self.stdout.write('Dummy reports created!')
