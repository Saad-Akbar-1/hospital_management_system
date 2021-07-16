"""
Apps.py where apps are registered.
"""
from django.apps import AppConfig

class PatientConfig(AppConfig):
    """Configuration for Patient."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'patient'
