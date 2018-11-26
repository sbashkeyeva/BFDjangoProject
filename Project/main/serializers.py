from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class CustomerModelSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class CityModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password",)


class ShopModelSerializer(serializers.ModelSerializer):
    city = CityModelSerializer(read_only=True)

    class Meta:
        model = Shop
        fields = "__all__"


class FlowerModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flower
        fields =['name','description']


class ShopFlowerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopFlower
        fields = "__all__"

