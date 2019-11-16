from rest_framework import serializers
from .models import *

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('cust_id','cust_FName','cust_LName','phoneNo','cust_ssn','cust_address1',
                    'cust_address2','cust_country','cust_zip')


# class EmployeeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Employee
#         fields = ('emp_id','emp_FName','emp_LName','phoneNo','emp_ssn','emp_address1',
#                     'emp_address2','emp_country','emp_zip')
#
# class StockSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Stock
#         fields = ('symbol','stock_fullname','stock_price','recent_price','recent_date')
#
# class WatchListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = WatchList
#         fields = ('user', 'watchlist_id', 'created_date')
#         depth = 1
#
# class WatchStockSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = watchListStock
#         fields = ('watchList','stock','added_date')
#         depth = 1
#
