# Generated by Django 5.0.6 on 2024-06-13 02:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0008_alter_user_gender_alter_user_mobile'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalHistory',
            fields=[
                ('mhid', models.AutoField(primary_key=True, serialize=False)),
                ('allergies', models.CharField(blank=True, max_length=100, null=True, verbose_name='Allergies')),
                ('medications', models.CharField(blank=True, max_length=100, null=True, verbose_name='Medications')),
                ('surgeries', models.CharField(blank=True, max_length=100, null=True, verbose_name='Surgeries')),
                ('family_medical_history', models.CharField(blank=True, max_length=100, null=True, verbose_name='Family Medical History')),
                ('life_style_factors', models.CharField(blank=True, max_length=100, null=True, verbose_name='Life Style Factor')),
                ('physical_examination', models.CharField(blank=True, max_length=100, null=True, verbose_name='Physical Examination')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Medical History Created')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Medical History Updated')),
                ('pid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.patient')),
            ],
            options={
                'verbose_name': 'MedicalHistory',
                'verbose_name_plural': 'MedicalHistories',
            },
        ),
    ]
