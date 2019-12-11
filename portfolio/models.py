from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
import requests
# from newsapi import NewsApiClient


# Create your models here.
class Customer(models.Model):
    cust_id = models.CharField(max_length=20,primary_key=True)
    cust_FName = models.CharField(max_length=50)
    cust_LName = models.CharField(max_length=50)
    phoneNo = models.IntegerField(blank=False,null=False)
    cust_ssn = models.IntegerField(blank=False,null=False)
    cust_address1 = models.CharField(max_length=300)
    cust_address2 = models.CharField(max_length=100,blank=True)
    cust_country = models.CharField(max_length=100)
    cust_zip = models.IntegerField(blank=False)

    def __str__(self):
        return str(self.cust_id)


class Employee(models.Model):
    emp_id = models.CharField(max_length=20,primary_key=True)
    emp_FName = models.CharField(max_length=100)
    emp_LName = models.CharField(max_length=100)
    phoneNo = models.IntegerField(blank=False,null=False)
    emp_ssn = models.IntegerField(blank=False,null=False)
    emp_address1 = models.CharField(max_length=300)
    emp_address2 = models.CharField(max_length=100, blank=True)
    emp_country = models.CharField(max_length=100)
    emp_zip = models.IntegerField(blank=False,null=False)

    def __str__(self):
        return str(self.emp_id)


class Stock(models.Model):
    symbol = models.CharField(max_length=10,blank=False,primary_key=True)
    stock_fullname = models.CharField(max_length=30)
    stock_price = models.DecimalField(max_digits=10,decimal_places=2)
    recent_price = models.DecimalField(max_digits=10,decimal_places=2)

    recent_date = models.DateField(default=timezone.now,null=False)

    def __str__(self):
        return str(self.symbol)

    def price_change(self):
        price_change = self.stock_price - self.recent_price
        return price_change


class WatchList(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer')
    watchlist_id = models.CharField(max_length=10,primary_key=True)
    created_date = models.DateField(default=timezone.now)

    def __str__(self):
        return str(self.watchlist_id)

class watchListStock(models.Model):
    watchList = models.ForeignKey(WatchList,on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='stock')
    added_date = models.DateField(default=timezone.now, null=False)

class Currency(models.Model):
    from_currency = models.CharField(max_length=10)
    to_currency = models.CharField(max_length=10)
    from_number = models.DecimalField(decimal_places=2, max_digits=8)
    rate = models.DecimalField()

    def rate(self):
        from_symbol = str(self.from_currency)
        to_symbol = str(self.to_currency)
        main_api = 'https://free.currconv.com/api/v7/convert?q='
        from_symbol = from_symbol.upper()
        to_symbol = to_symbol.upper()
        combined_symbol = from_symbol + '_' + to_symbol
        api_key = '&compact=ultra&apiKey=672e844f6f7acb1e8217'
        url = main_api + combined_symbol + api_key
        json_data = requests.get(url).json()
        rate = float(json_data[combined_symbol])
        return rate

    def to_number(self):
        to_number = float(self.from_number) * float(self.rate())
        return to_number






