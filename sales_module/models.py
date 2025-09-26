from django.db import models
from django.db.models import Max
from admin_module.models import Clients, Products
from users_module.models import Users


STATUS_CHOICES_PROCESS = (
    (1, 'En marcha'),
    (2, 'Suspendido'),
    (3, 'Finalizado')
)

STATUS_CHOICES_QUOTE = (
    (1, 'En Creación'),
    (2, 'Emitida'),
    (3, 'Aceptada'),
    (4, 'Rechazada'),
)

class Process(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.BooleanField(default=1, choices=STATUS_CHOICES_PROCESS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='process_quotes_created_by')
    updated_by = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='process_quotes_updated_by')

    class Meta:
        db_table = 'process_quotes'
        managed = True
        verbose_name = 'Proceso de Cotización'
        verbose_name_plural = 'Procesos de Cotizaciones'
        ordering = ['-updated_at']

class Quotes(models.Model):
    id = models.AutoField(primary_key=True)
    process = models.ForeignKey(Process, on_delete=models.CASCADE, related_name='quotes_process')
    client = models.ForeignKey(Clients, on_delete=models.CASCADE, related_name='quotes_client')
    date_quote = models.DateField()
    consecutive_number = models.IntegerField(min_value=1)
    consecutive = models.CharField(max_length=10, unique=True)    
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_iva = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.BooleanField(default=1, choices=STATUS_CHOICES_QUOTE)
    observations = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='quotes_created_by')
    updated_by = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='quotes_updated_by')

    def __str__(self):
        return self.consecutive

    def save(self, *args, **kwargs):
        if not self.consecutive:
            max_consecutive = Quotes.objects.aggregate(Max('consecutive_number'))['consecutive_number__max']
            self.consecutive_number = 1 if max_consecutive is None else max_consecutive + 1
            self.consecutive = f'COT-{self.consecutive_number}'
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'quotes'
        managed = True
        verbose_name = 'Cotización'
        verbose_name_plural = 'Cotizaciones'
        ordering = ['-updated_at']

class ItemsQuote(models.Model):
    id = models.AutoField(primary_key=True)
    quote = models.ForeignKey(Quotes, on_delete=models.CASCADE, related_name='items_quote')
    process = models.ForeignKey(Process, on_delete=models.CASCADE, related_name='items_quote_process')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='items_quote_product')
    quantity = models.IntegerField(min_value=1)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_iva = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.product.name

    def save(self, *args, **kwargs):
        self.subtotal = self.quantity * self.product.price
        if self.product.taxes:
            self.total_iva = self.subtotal * self.product.value_taxes
        else:
            self.total_iva = 0
        self.total = self.subtotal + self.total_iva
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'items_quote'
        managed = True
        verbose_name = 'Item de Cotización'
        verbose_name_plural = 'Items de Cotizaciones'
        ordering = ['-updated_at']