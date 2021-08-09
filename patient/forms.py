'''
The signup form design for Patient Model.
'''
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import EmailValidator, RegexValidator
from phonenumber_field.modelfields import PhoneNumberField

from patient.models import Patient


class SignUpForm(forms.ModelForm):
    '''The custom signup form class for Patient Model'''
    alphabets = RegexValidator(r'^[a-zA-Z]*$', 'Only alphabets are allowed.')
    patient_contact = PhoneNumberField(max_length=15)
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES, widget=forms.RadioSelect)
    ADMITTED, IN_PROGRESS, UNDER_OPERATION, DISCHARGED = 'A', 'I', 'U', 'D'
    status_choices = [(ADMITTED, 'Admitted'), (IN_PROGRESS, 'In Progress'),
                      (UNDER_OPERATION, 'Under Operation'), (DISCHARGED, 'Discharged')]
    status = forms.ChoiceField(
        choices=status_choices, widget=forms.RadioSelect)

    class Meta:
        '''Overriding the base class meta'''
        model = Patient
        fields = ('patient_name',
                  'patient_contact', 'birth_date', 'gender',
                  'status'
                  )
