from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from main.serializers import ShopModelSerializer
from main.models import Shop


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
    def get_object(self, pk):
        try:
            return Shop.objects.get(id=pk)
        except Shop.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        shop=self.get_object(pk)
        serializer=ShopModelSerializer(shop)
        return Response(serializer.data)

    def put(self,request,pk):
        shop=self.get_object(pk)
        serializer=ShopModelSerializer(instance=shop,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        shop=self.get_object(pk)
        shop.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


