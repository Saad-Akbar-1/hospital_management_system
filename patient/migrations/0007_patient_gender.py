# Generated by Django 3.2.5 on 2021-07-19 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0006_patient_birth_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='gender',
            field=models.CharField(
                choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1),
        ),
    ]
