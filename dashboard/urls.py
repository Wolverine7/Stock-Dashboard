from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.conf.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('dashboard/', TemplateView.as_view(template_name="application.html"), name="app"),
    path('',TemplateView.as_view(template_name="index.html"), name="app"),
    path('portfolio', include('portfolio.urls', namespace='portfolio')),

]