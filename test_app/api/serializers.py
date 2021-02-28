from rest_framework import serializers
from .models import City, Department, Region


class CitySerializer(serializers.ModelSerializer):
    department = serializers.SerializerMethodField('get_department')
    region = serializers.SerializerMethodField('get_region')
    postcodes = serializers.SerializerMethodField('format_postcodes')

    class Meta:
        model = City
        fields = ('name', 'code', 'postcodes', 'population', 'department', 'region')

    def get_department(self, obj):
        return obj.department.name

    def get_region(self, obj):
        return obj.region.name

    def format_postcodes(self, obj):
        return obj.postcodes.split(',')


class DepartmentSerializer(serializers.ModelSerializer):
    region = serializers.SerializerMethodField('get_region')

    class Meta:
        model = Department
        fields = ('name', 'code', 'region')

    def get_region(self, obj):
        return obj.region.name


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('name', 'code')
