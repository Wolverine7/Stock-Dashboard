from rest_framework import serializers
from .models import *

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


# class EmployeeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Employee
#         fields = '__all__'
#
class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'
#
# class WatchListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = WatchList
#         fields = '__all__'
#         depth = 1
#
# class WatchStockSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = watchListStock
#         fields = '__all__'
#         depth = 1
#
