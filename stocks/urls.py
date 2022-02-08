from django.urls import path


from .views import StockListView, GranularStockListView, StockListApiView

urlpatterns = [
    path("stocks/", StockListView.as_view()),
    path("stocks-granular/", GranularStockListView.as_view()),
    path("stock-filter/", StockListApiView.as_view()),
]
