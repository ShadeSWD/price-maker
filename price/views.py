from rest_framework import viewsets
from price.models import Price
from price.serializers import PriceSerializer
from price.paginators import PricePagination
from price.permissions import IsVendor


class PriceViewSet(viewsets.ModelViewSet):
    serializer_class = PriceSerializer
    pagination_class = PricePagination
    permission_classes = [IsVendor, ]
    queryset = Price.objects.all()

    def perform_create(self, serializer):
        super().perform_create(serializer)
        new = serializer.save()
        new.owner = self.request.user
        new.save()
