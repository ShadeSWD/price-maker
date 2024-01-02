from django.db import models

NULLABLE = {"null": True, "blank": True}


class Price(models.Model):
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
        full_price = float(self.origin_price) * (1 + float(self.tax)) * ((1 + float(self.bank_commission)) ** 2) * \
                     (1 + float(self.shop_commission))
        return full_price
