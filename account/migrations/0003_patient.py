# Generated by Django 5.0.6 on 2024-06-08 02:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('aadhar', models.CharField(blank=True, max_length=100, null=True, verbose_name='Specialization')),
                ('pan', models.CharField(blank=True, max_length=100, null=True, verbose_name='Degree')),
                ('emergency_contact', models.CharField(blank=True, max_length=100, null=True, verbose_name='Degree')),
                ('insurance', models.CharField(blank=True, max_length=100, null=True, verbose_name='Degree')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Doctor Created')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Doctor updated')),
                ('uid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Patient',
                'verbose_name_plural': 'Patients',
            },
        ),
    ]
