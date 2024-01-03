from django.urls import path
from rest_framework.routers import DefaultRouter
from price.apps import PriceConfig
from price.views import PriceViewSet

app_name = PriceConfig.name

router = DefaultRouter()
router.register(r'prices', PriceViewSet, basename='prices')

urlpatterns = [] + router.urls
