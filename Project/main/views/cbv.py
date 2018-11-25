from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from main.serializers import CityModelSerializer, CustomerModelSerilizer, FlowerModelSerializer, ShopModelSerializer, \
    ShopFlowerModelSerializer
from main.models import City, Customer, Flower, Shop, ShopFlower
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated


class IsStaff(IsAuthenticated):
    def has_permission(self, request, view):
        return request.user or request.user.is_staff


class CityList(APIView):
    def get(self, request):
        city = City.objects.all()
        serializer = CityModelSerializer(city, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CityModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CityDetail(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated, IsStaff)

    def get_object(self, pk):
        try:
            return City.objects.get(id=pk)
        except City.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        city = self.get_object(pk)
        serializer = CityModelSerializer(city)
        return Response(serializer.data)

    def put(self, request, pk):
        city = self.get_object(pk)
        serializer = CityModelSerializer(instance=city, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        city = self.get_object(pk)
        city.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomerList(APIView):
    def get(self, request):
        customer = Customer.objects.all()
        serializer = CustomerModelSerilizer(customer, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomerModelSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerDetail(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated, IsStaff,)

    def get_object(self, pk):
        try:
            return Customer.objects.get(id=pk)
        except Customer.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        customer = self.get_object(pk)
        serializer = CustomerModelSerilizer(customer)
        return Response(serializer.data)

    def put(self, request, pk):
        customer = self.get_object(pk)
        serializer = CustomerModelSerilizer(instance=customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        customer = self.get_object(pk)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FlowerList(APIView):

    def get(self, request):
        flower = Flower.objects.all()
        serializer = FlowerModelSerializer(flower, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FlowerModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FlowerDetail(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated, IsStaff,)

    def get_object(self, pk):
        try:
            return Flower.objects.get(id=pk)
        except Flower.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        flower = self.get_object(pk)
        serializer = FlowerModelSerializer(flower)
        return Response(serializer.data)

    def put(self, request, pk):
        flower = self.get_object(pk)
        serializer = FlowerModelSerializer(instance=flower, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        flower = self.get_object(pk)
        flower.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ShopList(APIView):
    def get(self, request):
        shop = Shop.objects.all()
        serializer = ShopModelSerializer(shop, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ShopModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShopDetail(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated, IsStaff,)

    def get_object(self, pk):
        try:
            return Shop.objects.get(id=pk)
        except Shop.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        shop = self.get_object(pk)
        serializer = ShopModelSerializer(shop)
        return Response(serializer.data)

    def put(self, request, pk):
        shop = self.get_object(pk)
        serializer = ShopModelSerializer(instance=shop, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        shop = self.get_object(pk)
        shop.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ShopFlowerList(APIView):
    def get(self, request):
        shopFlower = ShopFlower.objects.all()
        serializer = ShopFlowerModelSerializer(shopFlower, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ShopFlowerModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShopFlowerDetail(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated, IsStaff,)

    def get_object(self, pk):
        try:
            return ShopFlower.objects.get(id=pk)
        except ShopFlower.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        shopFlower = self.get_object(pk)
        serializer = ShopFlowerModelSerializer(shopFlower)
        return Response(serializer.data)

    def put(self, request, pk):
        shopFlower = self.get_object(pk)
        serializer = ShopFlowerModelSerializer(instance=shopFlower, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        shop = self.get_object(pk)
        shop.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
