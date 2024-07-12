# Generated by Django 5.0.7 on 2024-07-12 16:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0008_alter_user_gender_alter_user_mobile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('invid', models.AutoField(primary_key=True, serialize=False)),
                ('invoice_date', models.DateField(verbose_name='Invoice Date')),
                ('total_amount', models.FloatField(blank=True, max_length=100, null=True, verbose_name='Total Amount')),
                ('total_gst', models.FloatField(blank=True, max_length=100, null=True, verbose_name='Total GST')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Invoice Created')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Invoice Updated')),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.patient')),
            ],
            options={
                'verbose_name': 'Invoice',
                'verbose_name_plural': 'Invoices',
            },
        ),
        migrations.CreateModel(
            name='InvoiceItem',
            fields=[
                ('itemid', models.AutoField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Item Name')),
                ('quantity', models.FloatField(blank=True, max_length=100, null=True, verbose_name='Quantity')),
                ('amount', models.FloatField(blank=True, max_length=100, null=True, verbose_name='Amount')),
                ('gst', models.FloatField(blank=True, max_length=100, null=True, verbose_name='GST')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Invoice Item Created')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Invoice Item Updated')),
                ('invid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.invoice')),
            ],
            options={
                'verbose_name': 'Invoice Item',
                'verbose_name_plural': 'Invoice Items',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payid', models.AutoField(primary_key=True, serialize=False)),
                ('payment_type', models.CharField(blank=True, choices=[('Cash', 'CASH'), ('Online', 'ONLINE')], max_length=100, null=True, verbose_name='Payment Type')),
                ('payment_note', models.CharField(blank=True, max_length=100, null=True, verbose_name='Payment Note')),
                ('amount', models.FloatField(blank=True, max_length=100, null=True, verbose_name='Amount')),
                ('payment_date', models.DateField(blank=True, max_length=100, null=True, verbose_name='Payment Date')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Payment Created')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Payment Updated')),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.patient')),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
            },
        ),
        migrations.AddField(
            model_name='invoice',
            name='payid',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='payment.payment'),
        ),
    ]