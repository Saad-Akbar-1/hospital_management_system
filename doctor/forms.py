'''
The signup form design for Doctor Model.
'''

from django import forms
from django.core.validators import RegexValidator

from doctor.models import Doctor


class SignUpForm(forms.ModelForm):
    '''The custom signup form class for Doctor Model'''
    alphabets = RegexValidator(r'^[a-zA-Z]*$', 'Only alphabets are allowed.')
    username = forms.CharField(max_length=30, validators=[alphabets])
    password = forms.CharField(widget=forms.PasswordInput())
    fullname = forms.CharField(max_length=200)
    profilepic = forms.ImageField()

    class Meta:
        '''Overriding the base class meta'''
        model = Doctor
        fields = ('username', 'password',
                  'fullname', 'profilepic',
                  'specialisation'
                  )
