from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.conf.urls import *
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="application.html"), name="app"),
    path('', include('portfolio.urls', namespace='portfolio')),
    url(r'^auth/obtain_token/', obtain_jwt_token),
    url(r'^auth/refresh_token/', refresh_jwt_token),
]

