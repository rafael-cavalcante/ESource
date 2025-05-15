from django.urls import path
from ESource.views import views_dashboard

urlpatterns = [
    path('dashboard', views_dashboard.exibir_dashboard, name='dashboard'),
]