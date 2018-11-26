from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.serializers import CustomerModelSerilizer,CityModelSerializer,FlowerModelSerializer,ShopModelSerializer,ShopFlowerModelSerializer

from main.models import Customer,City,Flower,Shop,ShopFlower
from django.shortcuts import render, redirect


@api_view(['GET', 'POST'])
def customer_list(request):
    if request.method == 'GET':
        customers = Customer.objects.all()
        serializer = CustomerModelSerilizer(customers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CustomerModelSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'PUT', 'DELETE'])
def customer_detail(request, pk):
    try:
        customer = Customer.objects.get(id=pk)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomerModelSerilizer(customer)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CustomerModelSerilizer(instance=customer, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET',  'PUT'])
def city_list(request):
    if request.method == 'GET':
        cities = City.objects.all()
        serializer = CityModelSerializer(cities, many=True)
        context = {
            'cities': cities
        }
        return render(request, 'cities.html', context)

    elif request.method == 'POST':
        serializer = CityModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'PUT', 'DELETE'])
def city_detail(request, pk):
    try:
        city = City.objects.get(id=pk)
    except City.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CityModelSerializer(city)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CityModelSerializer(instance=city, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        city.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def flower_list(request):
    if request.method == 'GET':
        flowers = Flower.objects.all()
        serializer = FlowerModelSerializer(flowers, many=True)
        context = {
            'flowers': flowers
        }
        return render(request, 'flower.html', context)

    elif request.method == 'POST':
        serializer = FlowerModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return render(request, 'flower.html')
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'PUT', 'DELETE'])
def flower_detail(request, pk):
    try:
        flower = Flower.objects.get(id=pk)
    except Flower.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FlowerModelSerializer(flower)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = FlowerModelSerializer(instance=flower, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        flower.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
def shop_list(request):
    if request.method == 'GET':
        shops = Shop.objects.all()
        serializer = ShopModelSerializer(shops, many=True)
        context = {
            'shops': shops
        }
        return render(request, 'shop.html', context)

    elif request.method == 'POST':
        serializer = ShopModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'PUT', 'DELETE'])
def shop_detail(request, pk):
    try:
        shop = Shop.objects.get(id=pk)
    except Shop.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ShopModelSerializer(shop)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ShopModelSerializer(instance=shop, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        shop.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def shopflower_list(request):
    if request.method == 'GET':
        shopflowers = ShopFlower.objects.all()
        serializer = ShopFlowerModelSerializer(shopflowers, many=True)
        return render(request, 'base.html')
    elif request.method == 'POST':
        serializer = ShopFlowerModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'PUT', 'DELETE'])
def shopflower_detail(request, pk):
    try:
        shopflowers = ShopFlower.objects.get(id=pk)
    except ShopFlower.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ShopFlowerModelSerializer(shopflowers)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ShopFlowerModelSerializer(instance=shopflowers, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        shopflowers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
