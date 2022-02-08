from rest_framework.serializers import ModelSerializer

from .models import Company, PriceLookUpEvent


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = (
            "periodic_task",
            "id",
            "name",
            "stock_name",
            "timestamp",
            "scraping_scheduler_enabled",
            "has_granular_scraping",
            "one_off_scrape",
        )


class StockPriceSerializer(ModelSerializer):
    company = CompanySerializer()

    class Meta:
        model = PriceLookUpEvent
        fields = ("company", "stock_name", "price", "source")
