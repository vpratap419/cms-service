# Generated by Django 5.0.6 on 2024-06-08 02:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0005_alter_patient_aadhar_alter_patient_created_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('rid', models.AutoField(primary_key=True, serialize=False)),
                ('reason_for_visit', models.CharField(blank=True, max_length=100, null=True, verbose_name='ReasonForVisit')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Registration Created')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Registration updated')),
                ('did', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='patient_doctor_registration', to='account.doctor', verbose_name='Doctor')),
                ('pid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.patient')),
            ],
            options={
                'verbose_name': 'Registration',
                'verbose_name_plural': 'Registrations',
            },
        ),
    ]
