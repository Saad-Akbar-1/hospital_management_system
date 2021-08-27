"""Delete dummy doctors for testing purpose."""

from django.core.management.base import BaseCommand

from doctor.models import Doctor


class Command(BaseCommand):
    """Delete dummy doctors command class."""

    help = "Delete dummy doctors for clean database."

    def handle(self, *args, **kwargs):
        """Delete dummy doctors from database."""
        Doctor.objects.filter(fullname__startswith="Dummy").delete()
        self.stdout.write('Dummy doctors deleted successfully.')