# Generated by Django 5.0.6 on 2024-06-13 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emr', '0002_prescription_medication_testreport'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='medicalhistory',
            options={'verbose_name': 'Medical History', 'verbose_name_plural': 'Medical Histories'},
        ),
    ]
