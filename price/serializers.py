from rest_framework import serializers
from price.models import Price


class PriceSerializer(serializers.ModelSerializer):
    full_price = serializers.SerializerMethodField

    def get_full_price(self, obj):
        return obj.full_price

    class Meta:
        model = Price
        fields = ['origin_price', 'full_price', 'tax', 'bank_commission', 'shop_commission']
