# Generated by Django 5.0.6 on 2024-06-13 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emr', '0003_alter_medicalhistory_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medication',
            name='dosage',
            field=models.CharField(blank=True, choices=[('Daily', 'Daily'), ('Weekly', 'Weekly')], max_length=100, null=True, verbose_name='Dosage'),
        ),
        migrations.AlterField(
            model_name='testreport',
            name='test_report',
            field=models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Available', 'Available')], max_length=100, null=True, verbose_name='Test Report'),
        ),
    ]
