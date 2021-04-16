from django.urls import path,include
from .views import GetAllData


app_name='book'


urlpatterns = [
    path('get-all-data/',GetAllData.as_view(),name='get-all-data'),
]
