'''
The signup form design for Patient Model.
'''
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import EmailValidator, RegexValidator
from phonenumber_field.modelfields import PhoneNumberField

from patient.models import Patient


class SignUpForm(UserCreationForm):
    '''The custom signup form class for Patient Model'''
    alphabets = RegexValidator(r'^[a-zA-Z]*$', 'Only alphabets are allowed.')
    patient_name = forms.CharField(max_length=30,validators=[alphabets])
    patient_email = forms.EmailField(max_length=200,validators=[EmailValidator])
    patient_contact = PhoneNumberField(max_length=15)
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect)
    class Meta:
        '''Overriding the base class meta'''
        model = Patient
        fields = ('patient_name', 'patient_email',
                 'patient_contact','birth_date','gender'
                 )
