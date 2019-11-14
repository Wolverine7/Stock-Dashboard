from django.contrib import admin
from .models import *


# Register your models here.
class CustomerList(admin.ModelAdmin):
    list_display = ('cust_id','cust_FName','cust_LName','phoneNo','cust_ssn','cust_address1',
                    'cust_address2','cust_country','cust_zip')
    list_filter = ('cust_id', 'cust_FName', 'cust_LName', 'cust_zip')
    search_fields = ('cust_id', 'cust_FName', 'cust_LName')
    ordering = ['cust_id']


class EmployeeList(admin.ModelAdmin):
    list_display =('emp_id','emp_FName','emp_LName','phoneNo','emp_ssn','emp_address1',
                    'emp_address2','emp_country','emp_zip')
    list_filter = ('emp_id', 'emp_FName', 'emp_LName', 'emp_zip')
    search_fields = ('emp_id', 'emp_FName', 'emp_LName')
    ordering = ['emp_id']


class StockList(admin.ModelAdmin):
    list_display = ('symbol','stock_fullname','stock_price','recent_price','recent_date')
    list_filter = ('symbol', 'stock_fullname', 'stock_price', 'recent_price')
    search_fields = ('symbol', 'stock_fullname')
    ordering = ['symbol']


class WatchListAdmin(admin.ModelAdmin):
    list_display = ('user','watchlist_id','created_date')
    list_filter = ('user', 'watchlist_id', 'created_date')
    search_fields = ('user','watchlist_id')
    ordering = ['watchlist_id']

class WatchStockList(admin.ModelAdmin):
    list_display = ('watchList','stock','added_date')
    list_filter = ('watchList', 'stock', 'added_date')
    search_fields = ('watchlist','stock')
    ordering = ['added_date']


admin.site.register(Customer, CustomerList)
admin.site.register(Employee, EmployeeList)
admin.site.register(Stock, StockList)
admin.site.register(WatchList, WatchListAdmin)
admin.site.register(watchListStock, WatchStockList)
