from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from main import views

urlpatterns = [
    path('city/list/', views.CityList.as_view()),
    path('city/detail/', views.CityDetail.as_view()),
    path('customer/list/', views.CustomerList.as_view()),
    path('customer/detail/', views.CustomerDetail.as_view()),
    path('flower/list/', views.FlowerList.as_view()),
    path('flower/detail/', views.FlowerDetail.as_view()),
    path('city/list/', views.ShopList.as_view()),
    path('city/detail/', views.ShopDetail.as_view()),
    path('city/list/', views.ShopFlowerList.as_view()),
    path('city/detail/', views.ShopFlowerDetail.as_view()),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)