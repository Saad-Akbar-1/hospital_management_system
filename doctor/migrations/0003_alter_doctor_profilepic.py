# Generated by Django 3.2.5 on 2021-07-29 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_alter_doctor_profilepic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='profilepic',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
    ]