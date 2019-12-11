from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from .serializers import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.contrib.auth.models import User
import requests


# Create your views here.

# Welcome page

# Customer API
@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes(IsAuthenticatedOrReadOnly)
def customer_list(request):
    if request.method == 'GET':
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, context={'request': request}, many=True)
        return Response({'data': serializer.data})

    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def getCustomer(request, pk):
    """
    Retrieve, update or delete a customer instance.
    """
    try:
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomerSerializer(customer, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CustomerSerializer(customer, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Stock API
@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes(IsAuthenticatedOrReadOnly)
def stock_list(request):
    permission_classes = (IsAuthenticatedOrReadOnly)
    if request.method == 'GET':
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, context={'request': request}, many=True)
        return Response({'data': serializer.data})

    elif request.method == 'POST':
        serializer = StockSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def getStock(request, pk):
    """
    Retrieve, update or delete a customer instance.
    """
    try:
        stock = Stock.objects.get(pk=pk)
    except Stock.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StockSerializer(stock, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StockSerializer(stock, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        stock.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def getNewsFeed():
    mainapi = "https://newsapi.org/v2/top-headlines?country=us&apiKey="
    API_KEY = "0f4f674423984c8e8f60d2e4daac80d2"
    url = mainapi + API_KEY
    json_data = requests.get(url).json()
    title = []
    author = []
    des = []
    i = 0
    for i in range(5):
        title = title.append(json_data["articles"][i]["title"])
        author = author.append(json_data["articles"][i]["author"])
        des = des.append(json_data["articles"][i]["description"])


# def getDataTrend(request, *args, **kwargs):

from rest_framework.decorators import api_view

@api_view()
def getDataTrend(request):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo'
    trendline_json_data = json_data = requests.get(url).json()
    return Response(trendline_json_data)

@api_view()
def getDataTable(request):
    url = 'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=Micro&apikey=demo'
    table_json_data = json_data = requests.get(url).json()
    return Response(table_json_data)
