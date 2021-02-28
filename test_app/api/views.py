from rest_framework import status
import requests
from .serializers import CitySerializer, DepartmentSerializer, RegionSerializer
from .models import City, Department, Region
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Use of generic django views rather than DRF views

def index(request):
    # I made the logic there for the listing interface so I could easily use the pagination, working on huge set of data
    # I did not used the api routes though
    searched = request.GET.get('search', '')
    cities = City.objects.filter(Q(name__icontains=searched) | Q(postcodes__icontains=searched))
    page = request.GET.get('page', 1)
    paginator = Paginator(cities, 100)
    page_range = 10
    try:
        cities = paginator.page(page)
        page_range = range(max(int(page) - 5, 2), min(int(page) + 5, int(cities.paginator.num_pages) - 1))
    except PageNotAnInteger:
        cities = paginator.page(1)
    except EmptyPage:
        cities = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'cities': cities, 'searched': searched, 'page_range': page_range})


# CRUD For city Model

def city_list_create(request):
    # get list of cities
    if request.method == 'GET':
        searched = request.GET.get('search', '')
        cities = City.objects.filter(Q(name__icontains=searched) | Q(postcodes__icontains=searched))
        serializer = CitySerializer(cities, many=True)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})

    # create a new city
    elif request.method == 'POST':

        city = City()

        city.name = request.POST.get('name')
        city.code = request.POST.get('code')
        city.postcodes = request.POST.get('postcodes')
        city.population = request.POST.get('population')
        city.department = Department.objects.get(code=request.POST.get('departmentCode'))
        city.region = Region.objects.get(code=request.POST.get('regionCode'))
        city.save()

        serializer = CitySerializer(city)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})


def city_get_delete_update(request, code):

    try:
        city = City.objects.get(code=code)
    except City.DoesNotExist:
        return JsonResponse({'error': 'city code {0} not found'.format(code)}, status=status.HTTP_404_NOT_FOUND)

    # get details of a single city
    if request.method == 'GET':
        serializer = CitySerializer(city)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})

    # delete a single city
    elif request.method == 'DELETE':
        city.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

    # update details of a single city
    elif request.method == 'PUT':

        city.name = request.POST.get('nom', city.name)
        city.code = request.POST.get('code', city.code)
        city.postcodes = request.POST.get('postcodes'), city.postcodes
        city.population = request.POST.get('population', city.population)
        city.department = Department.objects.get(code=request.POST.get('departmentCode'))
        city.region = Region.objects.get(code=request.POST.get('regionCode'))
        city.save()

        serializer = CitySerializer(city)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})


# NOT REQUESTED
# Get For Department and Regions Models

def department_list(request):
    # get all departments
    if request.method == 'GET':
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})


def department_get(request, code):
    # get one department
    if request.method == 'GET':

        try:
            department = Department.objects.get(code=code)
        except Department.DoesNotExist:
            return JsonResponse({'error': 'dep. code {0} not found'.format(code)}, status=status.HTTP_404_NOT_FOUND)

        serializer = DepartmentSerializer(department)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})


def region_list(request):
    # get all regions
    if request.method == 'GET':
        regions = Region.objects.all()
        serializer = RegionSerializer(regions, many=True)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})


def region_get(request, code):
    # get one region
    if request.method == 'GET':

        try:
            region = Region.objects.get(code=code)
        except Region.DoesNotExist:
            return JsonResponse({'error': 'region code {0} not found'.format(code)}, status=status.HTTP_404_NOT_FOUND)

        serializer = RegionSerializer(region)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})
