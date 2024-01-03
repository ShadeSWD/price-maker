from rest_framework.pagination import PageNumberPagination


class PricePagination(PageNumberPagination):
    page_size = 50
