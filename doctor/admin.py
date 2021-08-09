from django.contrib import admin
from doctor.models import Doctor


class DoctorAdmin(admin.ModelAdmin):
    '''Customizing the view for admin here'''
    list_display = ('fullname', 'specialisation')
    fieldsets = [
        (None,               {'fields': ['fullname']}),
        ('Email', {'fields': ['specialisation']}),
    ]
    list_filter = ['fullname']
    search_fields = ['fullname','specialisation']

admin.site.register(Doctor,DoctorAdmin)