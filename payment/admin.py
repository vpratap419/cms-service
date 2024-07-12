from django.contrib import admin
from payment.models import Payment, Invoice, InvoiceItem


# Register your models here.
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('payid', 'pid', 'payment_type', 'payment_note', 'amount', 'payment_date')


admin.site.register(Payment, PaymentAdmin)


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invid', 'pid', 'payid', 'invoice_date', 'total_amount', 'total_gst')


admin.site.register(Invoice, InvoiceAdmin)


class InvoiceItemAdmin(admin.ModelAdmin):
    list_display = ('itemid', 'invid', 'item_name', 'quantity', 'amount', 'gst')


admin.site.register(InvoiceItem, InvoiceItemAdmin)


