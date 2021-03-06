# Generated by Django 3.2.5 on 2021-08-06 07:16

import django.db.models.deletion
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('patient_name', models.CharField(max_length=200)),
                ('admission_date', models.DateTimeField(verbose_name='Date of Admission')),
                ('patient_contact', phonenumber_field.modelfields.PhoneNumberField(max_length=15, region=None)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1)),
                ('status', models.CharField(choices=[('A', 'Admitted'), ('I', 'In Progress'), ('U', 'Under Operation'), ('D', 'Discharged')], default='A', max_length=1)),
                ('concerned_doctor', models.ForeignKey(blank=True, help_text='Assign the Doctor', null=True, on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor')),
            ],
        ),
    ]
