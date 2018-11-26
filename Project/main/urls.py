from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from main import views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('register/', views.register),
    path('city/list/', views.CityList.as_view()),
    path('city/detail/<int:pk>/', views.CityDetail.as_view()),
    path('customer/list/', views.CustomerList.as_view()),
    path('customer/detail/<int:pk>/', views.CustomerDetail.as_view()),
    path('flower/list/', views.FlowerList.as_view()),
    path('flower/detail/<int:pk>/', views.FlowerDetail.as_view()),
    path('shop/list/', views.ShopList.as_view()),
    path('shop/detail/<int:pk>/', views.ShopDetail.as_view()),
    path('shop/flower/list/', views.ShopFlowerList.as_view()),
    path('shop/flower/detail/<int:pk>/', views.ShopFlowerDetail.as_view()),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
