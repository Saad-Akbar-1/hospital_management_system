"""Delete dummy reports for testing purpose."""

from django.core.management.base import BaseCommand

from lab.models import Reports
from lab.models import Doctor


class Command(BaseCommand):
    """Delete dummy reports command class."""

    help = "Delete dummy reports for clean database."

    def handle(self, *args, **kwargs):
        """Delete dummy doctors from database."""
        dummy_doctor_list =Doctor.objects.filter(fullname__startswith="Dummy")
        for obj in dummy_doctor_list:
            Reports.objects.get(concerned_doctor=obj.id).delete()
        self.stdout.write('Dummy reports deleted successfully.')