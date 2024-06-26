# Generated by Django 5.0.6 on 2024-06-13 13:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_alter_user_gender_alter_user_mobile'),
        ('emr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('prid', models.AutoField(primary_key=True, serialize=False)),
                ('prescription_date', models.DateField(auto_now_add=True, verbose_name='Prescription Date')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Prescription Created')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Prescription Updated')),
                ('did', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.doctor')),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.patient')),
            ],
            options={
                'verbose_name': 'Prescription',
                'verbose_name_plural': 'Prescriptions',
            },
        ),
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('mid', models.AutoField(primary_key=True, serialize=False)),
                ('medication_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Medication Name')),
                ('dosage_instruction', models.CharField(blank=True, max_length=100, null=True, verbose_name='Dosage Instruction')),
                ('dosage', models.CharField(blank=True, choices=[('DAILY', 'Daily'), ('WEEKLY', 'Weekly')], max_length=100, null=True, verbose_name='Dosage')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Test Report Created')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Test Report Updated')),
                ('prid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emr.prescription')),
            ],
            options={
                'verbose_name': 'Medication',
                'verbose_name_plural': 'Medications',
            },
        ),
        migrations.CreateModel(
            name='TestReport',
            fields=[
                ('trid', models.AutoField(primary_key=True, serialize=False)),
                ('test_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Test Name')),
                ('test_instruction', models.CharField(blank=True, max_length=100, null=True, verbose_name='Test Instruction')),
                ('test_report', models.CharField(blank=True, choices=[('PENDING', 'Pending'), ('AVAILABLE', 'Available')], max_length=100, null=True, verbose_name='Test Report')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Test Report Created')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Test Report Updated')),
                ('prid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emr.prescription')),
            ],
            options={
                'verbose_name': 'Test Report',
                'verbose_name_plural': 'Test Reports',
            },
        ),
    ]
