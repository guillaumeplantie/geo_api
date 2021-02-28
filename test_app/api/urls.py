from django.urls import include, path
from . import views

urlpatterns = [
    # The index is the interface where the cities are displayed and the user can search
    path('', views.index),
    # CRUD for cities
    path('cities/', views.city_list_create),
    path('cities/<code>', views.city_get_delete_update),
    # Simple endpoints to get departments and regions (was not requested)
    path('departments/', views.department_list),
    path('departments/<code>', views.department_get),
    path('regions/', views.region_list),
    path('regions/<code>', views.region_get),
    # ...
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]