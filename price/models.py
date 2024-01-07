from django.db import models
from config import settings

NULLABLE = {"null": True, "blank": True}


class Price(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='owner', **NULLABLE)
    created_at = models.DateTimeField(verbose_name='creation date', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='change date', auto_now=True)
    origin_price = models.DecimalField(verbose_name='origin price', max_digits=20, decimal_places=6)
    tax = models.FloatField(default=0.06, verbose_name='tax value')
    bank_commission = models.FloatField(default=0.02, verbose_name='bank commission')
    shop_commission = models.FloatField(default=0.2, verbose_name='shop commission')

    def __str__(self):
        return f'{self.origin_price} -> {self.full_price}'

    class Meta:
        verbose_name = 'price'
        verbose_name_plural = 'prices'

    @property
    def full_price(self) -> float:
        origin_price = float(self.origin_price)
        tax = float(self.tax)
        bank_commission = float(self.bank_commission)
        shop_commission = float(self.shop_commission)

        tax_value = origin_price * tax
        shop_profit = origin_price * shop_commission
        shop_bank_commission = origin_price * bank_commission
        customer_bank_commission = (origin_price + tax_value + shop_bank_commission + shop_profit) * bank_commission
        full_price = origin_price + tax_value + shop_bank_commission + customer_bank_commission + shop_profit
        return full_price
