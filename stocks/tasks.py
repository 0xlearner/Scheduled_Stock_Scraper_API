import time
import datetime

# shared_task is ideal for Django
from celery import shared_task

from django.apps import apps

# from .models import PriceLookUpEvent
from .scraper import StockScraper


@shared_task
def hello_world(num=1):
    time.sleep(num)
    print(f"hello world {num}")


@shared_task
def perform_scrape(stock_name="AAPL", service="echo"):
    client = StockScraper(service=service)
    name, price = client.scrape(stock_name=stock_name)
    print("task", name, price)
    PriceLookUpEvent = apps.get_model("stocks", "PriceLookUpEvent")
    PriceLookUpEvent.objects.create_event(stock_name, price, name=name, source=service)


@shared_task
def company_price_scrape_task(instance_id, service="echo"):
    """
    Perform company price scraping event.
    """
    Company = apps.get_model("stocks", "Company")
    obj = Company.objects.get(id=instance_id)
    stock_name = obj.stock_name
    perform_scrape(stock_name=stock_name, service=service)


@shared_task
def company_granular_price_scrape_task(instance_id, service="echo"):
    """
    Perform company granular price scraping event.
    """
    Company = apps.get_model("stocks", "Company")
    obj = Company.objects.get(id=instance_id)
    stock_name = obj.stock_name
    perform_scrape(stock_name=stock_name, service=service)
    if obj.has_granular_scraping:
        now = datetime.datetime.now()
        expires = now + datetime.timedelta(seconds=65)
        for i in range(1, 60):
            perform_scrape.apply_async(
                kwargs={
                    "stock_name": stock_name,
                    "service": service,
                },
                coutndown=i,
                expires=expires,
            )
