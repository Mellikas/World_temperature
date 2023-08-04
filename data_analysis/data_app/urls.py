from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bar_chart/', views.bar_chart, name='bar_chart'),
    path('bar_chart_comparison/', views.bar_chart_comparison, name='bar_chart_comparison'),
    path('polar_area/', views.polar_area, name='polar_area'),
]