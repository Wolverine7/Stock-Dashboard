from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.conf.urls import include
from portfolio import views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('dashboard/', TemplateView.as_view(template_name="application.html"), name="app"),
    path('', TemplateView.as_view(template_name="index.html"), name="app"),
    # path('', views.welcome, name='home'),
    path('portfolio/', include('portfolio.urls', namespace='portfolio')),
    # JWT auth
    path('auth/', obtain_jwt_token)

]