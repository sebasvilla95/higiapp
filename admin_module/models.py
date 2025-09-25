from django.db import models
from users_module.models import Users

class Clients(models.Model):
    id = models.AutoField(primary_key=True)
    identification = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='clients_created_by')
    updated_by = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='clients_updated_by')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'admin_clients'
        managed = True
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

class Products(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='products_created_by')
    updated_by = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='products_updated_by')

    def __str__(self):
        return self.code

    class Meta:
        db_table = 'admin_products'
        managed = True
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
