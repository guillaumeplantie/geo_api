from django.db import models
# I did not implement the bonus
# from django.contrib.gis.db import models as gis_models


class Region(models.Model):
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=8, unique=True)


class Department(models.Model):
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=8, unique=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)


class City(models.Model):
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=8, unique=True)
    population = models.IntegerField()
    postcodes = models.CharField(max_length=64)
    # coordinates = gis_models.PointField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
