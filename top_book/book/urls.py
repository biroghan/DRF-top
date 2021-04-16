from django.urls import path,include
from .views import GetAllData,GetFavData,UpdateFavData,PostModelData,SearchData,DeleteData,allApi,SetData


app_name='book'


urlpatterns = [
    path('get-all-data/',GetAllData.as_view(),name='get-all-data'),
    path('all-data/',allApi,name='all-data'),
    path('get-fav-data/',GetFavData.as_view(),name='get-fav-data'),
    path('update-fav-data/<int:pk>/',UpdateFavData.as_view(),name='update-fav-data'),
    path('post-model/',PostModelData.as_view(),name='post-model'),
    path('set-data/',SetData,name='set-data'),
    path('search/',SearchData.as_view(),name='search'),
    path('delete/<int:pk>',DeleteData.as_view(),name='delete'),
]
