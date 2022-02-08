import json
import random
from requests_html import HTMLSession

SERVICES = {
    "business_insider": "https://markets.businessinsider.com/stocks/{stock_name}-stock",
    "google_finance": "https://www.google.com/finance/quote/{stock_name}:NASDAQ",
    "echo": "https://www.httpbin.org/anything/{stock_name}",
}

_session = HTMLSession()


class StockScraper:
    """
    Usage:

    StockScraper(service='echo', stock_name='AAPL').scrape()
    """

    service = "echo"
    url = None
    stock_name = "AAPL"

    def __init__(self, service="echo", stock_name="AAPL"):
        self.service = service
        self.url = SERVICES[service]
        self.stock_name = stock_name

    def scrape_business_insider(self, url=None):
        if url == None:
            return "", 0
        request = _session.get(url)
        extract_name = request.html.find("h1.price-section__identifiers")
        name = [n.text for n in extract_name][0].split(",")[0].strip()
        extract_price = request.html.find("span.price-section__current-value")
        price = float([p.text for p in extract_price][0].replace(",", "").strip())

        return name, price

    def scrape_google_finance(self, url=None):
        if url == None:
            return "", 0
        request = _session.get(url)
        name = request.html.find("div.zzDege")[0].text
        price = float(
            request.html.find("div.kf1m0")[0]
            .text.replace("$", "")
            .replace(",", "")
            .strip()
        )
        return name, price

    def scrape_echo(self, url=None):
        if url == None:
            return "", 0
        random_price = "%.2f" % (random.randint(0, 12000) / 100.00)
        request = _session.post(
            url, json={"stock_name": self.stock_name, "price": random_price}
        )
        data = json.loads(request.json()["data"])
        return data.get("stock_name"), data.get("price")

    def scrape(self, stock_name=None):
        to_scrape_stock_name = stock_name or self.stock_name
        if to_scrape_stock_name is None:
            to_scrape_stock_name = "AAPL"
        url = self.url.format(stock_name=to_scrape_stock_name)
        func = getattr(self, f"scrape_{self.service}")
        name, price = func(url)
        return name, price
