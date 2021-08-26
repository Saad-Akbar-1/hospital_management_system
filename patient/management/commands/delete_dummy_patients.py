"""Delete dummy patients for testing purpose."""

from django.core.management.base import BaseCommand

from patient.models import Patient


class Command(BaseCommand):
    """Delete dummy patients command class."""

    help = "Delete dummy patients for clean database."

    def handle(self, *args, **kwargs):
        """Delete dummy patients from database."""
        Patient.objects.filter(patient_name__startswith="dummy").delete()
        self.stdout.write('Dummy patients deleted successfully.')