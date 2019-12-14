from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from portfolio import views



app_name = 'portfolio'

urlpatterns = [

    # path('', views.welcome, name='welcome'),
    # url(r'^welcome/$', views.welcome, name='welcome'),

    path('admin/', admin.site.urls),
    path('auth/', obtain_jwt_token),

    # Customer api view
    path('customers/', views.customer_list),
    url(r'^api/customers/$', views.customer_list),
    url(r'^api/customers/(?P<pk>[0-9]+)$', views.getCustomer),

    # Stock api view
    path('stocks/',views.stock_list),
    url(r'^api/stocks/$', views.stock_list),
    url(r'^api/stocks/(?P<pk>[0-9]+)$', views.getStock),
    url('api/trendline', views.getDataTrend),
    url('api/table', views.getDataTable),
    url('api/mutipledata', views.getMultipleDataTrend),
    url('api/monthly', views.getDataOpenClose)
]