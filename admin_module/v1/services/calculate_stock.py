from admin_module.models import ManageStock
from django.db.models import Sum


class CalculateStock:
    """ Clase para calcular el stock de un producto dependiendo de los status choices """
    def __init__(self, product_id):
        self.product = product_id

    def calculate_stock(self):
        stock = ManageStock.objects.filter(product=self.product).values('status').annotate(total=Sum('quantity'))

        try:
            income = stock.filter(status=1)[0]['total']
        except:
            income = 0

        try:
            outcome = stock.filter(status=2)[0]['total']
        except:
            outcome = 0

        try:
            transfer = stock.filter(status=3)[0]['total']
        except:
            transfer = 0
            
        return income, outcome, transfer
            
            
            
            