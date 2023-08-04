from django.db.models import Q, Avg
from django.shortcuts import render
from .models import Temperature
from .data.data_chart_parameters import months, years, bar_backgroundcolor, bar_bordercolor

city = Temperature.objects.values_list("city", "country").distinct()


def home(request):
    labels = []
    values = []

    for year in years:
        query = Temperature.objects.filter(
            Q(year__icontains=year)).aggregate(Avg('avg_temp_C'))
        if query["avg_temp_C__avg"] is not None:
            labels.append(year)
            values.append(round(query["avg_temp_C__avg"], 2))
        else:
            labels.append(year)
            values.append(query["avg_temp_C__avg"])

    context = {
        "labels": labels,
        "values": values,
        "city":city,
        "years":years
    }
    return render(request, template_name='home.html', context=context)


def bar_chart(request):
    q_year = request.GET.get('query_year')
    q_city = request.GET.get('query_city')
    q_axis = request.GET.get('query_axis')
    labels = months
    values = []

    for month in months:
        query = Temperature.objects.filter(
            Q(month_name__icontains=month) &
            Q(year__icontains=q_year) &
            Q(city__icontains=q_city)).aggregate(Avg('avg_temp_C'))
        if query["avg_temp_C__avg"] is not None:
            values.append(round(query["avg_temp_C__avg"], 2))
        else:
            values.append(0)

    context = {
        'q_year': q_year,
        'q_city': q_city,
        'q_axis': q_axis,
        "labels": labels,
        "values": values,
        "bar_backgroundcolor":bar_backgroundcolor,
        "bar_bordercolor":bar_bordercolor
    }
    return render(request, template_name='bar_chart.html', context=context)

def bar_chart_comparison(request):
    q_year_1 = request.GET.get('query_year_1')
    q_city_1 = request.GET.get('query_city_1')
    q_year_2 = request.GET.get('query_year_2')
    q_city_2 = request.GET.get('query_city_2')
    q_year_3 = request.GET.get('query_year_3')
    q_city_3 = request.GET.get('query_city_3')
    q_axis = request.GET.get('query_axis')
    labels = months

    values_1 = []

    for month in months:
        query = Temperature.objects.filter(
            Q(month_name__icontains=month) &
            Q(year__icontains=q_year_1) &
            Q(city__icontains=q_city_1)).aggregate(Avg('avg_temp_C'))
        if query["avg_temp_C__avg"] is not None:
            values_1.append(round(query["avg_temp_C__avg"], 2))
        else:
            values_1.append(0)

    values_2 = []

    for month in months:
        query = Temperature.objects.filter(
            Q(month_name__icontains=month) &
            Q(year__icontains=q_year_2) &
            Q(city__icontains=q_city_2)).aggregate(Avg('avg_temp_C'))
        if query["avg_temp_C__avg"] is not None:
            values_2.append(round(query["avg_temp_C__avg"], 2))
        else:
            values_2.append(0)

    values_3 = []

    for month in months:
        query = Temperature.objects.filter(
            Q(month_name__icontains=month) &
            Q(year__icontains=q_year_3) &
            Q(city__icontains=q_city_3)).aggregate(Avg('avg_temp_C'))
        if query["avg_temp_C__avg"] is not None:
            values_3.append(round(query["avg_temp_C__avg"], 2))
        else:
            values_3.append(0)

    context = {
        'q_year_1': q_year_1,
        'q_city_1': q_city_1,
        'q_year_2': q_year_2,
        'q_city_2': q_city_2,
        'q_year_3': q_year_3,
        'q_city_3': q_city_3,
        'q_axis': q_axis,
        "labels": labels,
        "values_1": values_1,
        "values_2": values_2,
        "values_3": values_3,
        "bar_backgroundcolor": bar_backgroundcolor,
        "bar_bordercolor": bar_bordercolor
    }
    return render(request, template_name='bar_chart_comparison.html', context=context)

def polar_area(request):
    q_year = request.GET.get('query_year')
    q_city = request.GET.get('query_city')
    q_axis = request.GET.get('query_axis')
    labels = months
    values = []

    for month in months:
        query = Temperature.objects.filter(
            Q(month_name__icontains=month) &
            Q(year__icontains=q_year) &
            Q(city__icontains=q_city)).aggregate(Avg('avg_temp_C'))
        if query["avg_temp_C__avg"] is not None:
            values.append(round(query["avg_temp_C__avg"], 2))
        else:
            values.append(0)

    context = {
        'q_year': q_year,
        'q_city': q_city,
        'q_axis': q_axis,
        "labels": labels,
        "values": values,
    }
    return render(request, template_name='polar_area.html', context=context)
