import requests
import sys
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'test_app.settings'

import django
django.setup()

from django.db import IntegrityError
from api.models import Region, Department, City

if __name__ == "__main__":

    if "region" in sys.argv:

        r = requests.get('https://geo.api.gouv.fr/regions')
        if r.status_code == 200:
            for region in r.json():
                try:
                    oRegion = Region()
                    oRegion.name = region['nom']
                    oRegion.code = region['code']
                    oRegion.save()
                except IntegrityError:
                    pass
                except KeyError:
                    print(region)

    if "department" in sys.argv:

        r = requests.get('https://geo.api.gouv.fr/departements')
        if r.status_code == 200:
            for department in r.json():
                try:
                    oDepartment = Department()
                    oDepartment.name = department['nom']
                    oDepartment.code = department['code']
                    oDepartment.region = Region.objects.get(code=department['codeRegion'])
                    oDepartment.save()
                except (IntegrityError, Department.DoesNotExist):
                    pass
                except KeyError:
                    print(department)

    if "city" in sys.argv:

        r = requests.get('https://geo.api.gouv.fr/communes')
        if r.status_code == 200:
            for city in r.json():
                try:
                    oCity = City()
                    oCity.name = city['nom']
                    oCity.code = city['code']
                    oCity.postcodes = ','.join(city.get('codesPostaux'))
                    oCity.population = city.get('population')
                    oCity.department = Department.objects.get(code=city.get('codeDepartement'))
                    oCity.region = Region.objects.get(code=city.get('codeRegion'))
                    oCity.save()
                except (IntegrityError, Department.DoesNotExist, Region.DoesNotExist):
                    pass
                except KeyError:
                    print(city)
