# Generated by Django 3.2.5 on 2021-07-16 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_alter_patient_patient_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='admission_date',
            field=models.DateTimeField(verbose_name='Date of Admission'),
        ),
    ]