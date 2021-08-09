"""
Admin tab, customized to tailor to Patient module and CRUD operations
"""
from django.contrib import admin

from patient.models import Patient


class PatientAdmin(admin.ModelAdmin):
    '''Customizing the view for admin here'''
    list_display = ('patient_name', 'admission_date',
                    'patient_contact', 'is_admitted_recently')
    fieldsets = [
        (None,               {'fields': ['patient_name']}),
        ('Date information', {'fields': [
         'admission_date'], 'classes': ['collapse']}),
        ('Contact', {'fields': ['patient_contact']}),
        ('Concerned Doctor', {'fields': ['concerned_doctor']}),
        ('Status', {'fields': ['status']}),

    ]
    list_filter = ['admission_date']
    search_fields = ['patient_name']


admin.site.register(Patient, PatientAdmin)
