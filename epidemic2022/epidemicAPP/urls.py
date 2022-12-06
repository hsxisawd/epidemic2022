from django.urls import path
from . import views
urlpatterns = [
    path('get_province_add_top10_data/',views.get_province_add_top10_data),
    path('get_City_add_top10_data/',views.get_City_add_top10_data),
    path('get_province_RiskArea/',views.get_province_RiskArea),
    path('get_province_city_RiskArea/',views.get_province_city_RiskArea),
    path('get_province_city_add_comfirm/',views.get_province_city_add_comfirm),
    path('get_province_city_comfirm/',views.get_province_city_comfirm),
    path('get_China_data/',views.get_China_data),
    path('get_map_data/',views.get_map_Data)
]
