"""Delete dummy reports for testing purpose."""

from django.core.management.base import BaseCommand

from lab.models import Reports


class Command(BaseCommand):
    """Delete dummy reports command class."""

    help = "Delete dummy reports for clean database."

    def handle(self, *args, **kwargs):
        """Delete dummy doctors from database."""
        Reports.objects.filter(reporttype="CT").delete()
        self.stdout.write('Dummy reports deleted successfully.')