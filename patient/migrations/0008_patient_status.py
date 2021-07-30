# Generated by Django 3.2.5 on 2021-07-27 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0007_patient_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='status',
            field=models.CharField(choices=[('A', 'Admitted'), ('I', 'In Progress'), (
                'U', 'Under Operation'), ('D', 'Discharged')], default='A', max_length=1),
        ),
    ]