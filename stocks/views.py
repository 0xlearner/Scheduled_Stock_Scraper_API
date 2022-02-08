from rest_framework.generics import ListAPIView

from .models import Company, PriceLookUpEvent
from .serializers import StockPriceSerializer, CompanySerializer


class StockListView(ListAPIView):
    queryset = PriceLookUpEvent.objects.all()
    serializer_class = StockPriceSerializer


class GranularStockListView(ListAPIView):
    queryset = PriceLookUpEvent.objects.filter(company__has_granular_scraping=True)
    serializer_class = StockPriceSerializer


class StockListApiView(ListAPIView):
    queryset = PriceLookUpEvent.objects.all()
    serializer_class = StockPriceSerializer

    filter_fields = ("company__id",)
    search_fields = ("name",)
