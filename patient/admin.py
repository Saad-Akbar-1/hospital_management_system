"""
Admin tab, customized to tailor to Patient module and CRUD operations
"""
from django.contrib import admin

from patient.models import Patient  # pylint: disable=import-error


class PatientAdmin(admin.ModelAdmin):
    '''Customizing the view for admin here'''
    list_display = ('patient_name', 'admission_date', 'email',
                    'patient_contact', 'is_admitted_recently')
    fieldsets = [
        (None,               {'fields': ['patient_name']}),
        ('Date information', {'fields': [
         'admission_date'], 'classes': ['collapse']}),
        ('Email', {'fields': ['patient_email']}),
        ('Contact', {'fields': ['patient_contact']}),
    ]
    list_filter = ['admission_date']
    search_fields = ['patient_name']


admin.site.register(Patient, PatientAdmin)
