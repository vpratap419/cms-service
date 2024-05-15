# Generated by Django 5.0.6 on 2024-05-14 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128, verbose_name='Clinic Name')),
                ('contact', models.CharField(max_length=128, verbose_name='Clinic Contact')),
                ('address', models.CharField(max_length=1024, verbose_name='Clinic Address')),
                ('geolocation', models.CharField(max_length=128, verbose_name='Clinic Geolocation')),
                ('website', models.CharField(max_length=264, verbose_name='Clinic Website')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Clinic Created')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Clinic updated')),
            ],
            options={
                'verbose_name': 'Clinic',
                'verbose_name_plural': 'Clinics',
            },
        ),
    ]
