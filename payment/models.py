from django.db import models
from account.models import Patient

# Create your models here.

TYPE = (
    ('Cash', 'CASH'),
    ('Online', 'ONLINE'),
)


class Payment(models.Model):
    payid = models.AutoField(primary_key=True)
    pid = models.ForeignKey(Patient, on_delete=models.CASCADE)
    payment_type = models.CharField("Payment Type", choices=TYPE, max_length=100, null=True, blank=True)
    payment_note = models.CharField("Payment Note", max_length=100, null=True, blank=True)
    amount = models.FloatField("Amount", max_length=100, null=True, blank=True)
    payment_date = models.DateField("Payment Date", max_length=100, null=True, blank=True)
    created = models.DateTimeField("Payment Created", auto_now_add=True)
    updated = models.DateTimeField("Payment Updated", auto_now_add=True)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'

    def __str__(self):
        return '{} - {}'.format(self.payid, self.pid)


class Invoice(models.Model):
    invid = models.AutoField(primary_key=True)
    pid = models.ForeignKey(Patient, on_delete=models.CASCADE)
    payid = models.OneToOneField(Payment, on_delete=models.CASCADE)
    invoice_date = models.DateField("Invoice Date", )
    total_amount = models.FloatField("Total Amount", max_length=100, null=True, blank=True)
    total_gst = models.FloatField("Total GST", max_length=100, null=True, blank=True)
    created = models.DateTimeField("Invoice Created", auto_now_add=True)
    updated = models.DateTimeField("Invoice Updated", auto_now_add=True)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Invoice'
        verbose_name_plural = 'Invoices'

    def __str__(self):
        return '{} - {}'.format(self.invid, self.pid)


class InvoiceItem(models.Model):
    itemid = models.AutoField(primary_key=True)
    invid = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    item_name = models.CharField("Item Name", max_length=100, null=True, blank=True)
    quantity = models.FloatField("Quantity", max_length=100, null=True, blank=True)
    amount = models.FloatField("Amount", max_length=100, null=True, blank=True)
    gst = models.FloatField("GST", max_length=100, null=True, blank=True)
    created = models.DateTimeField("Invoice Item Created", auto_now_add=True)
    updated = models.DateTimeField("Invoice Item Updated", auto_now_add=True)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Invoice Item'
        verbose_name_plural = 'Invoice Items'

    def __str__(self):
        return '{} - {}'.format(self.itemid, self.invid)

