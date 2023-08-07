from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('line_chart/', views.line_chart, name='line_chart'),
    path('bar_chart/', views.bar_chart, name='bar_chart'),
    path('polar_area/', views.polar_area, name='polar_area'),
]