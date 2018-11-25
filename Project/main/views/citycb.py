from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from main.serializers import CityModelSerializer
from main.models import City


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
    def get_object(self, pk):
        try:
            return City.objects.get(id=pk)
        except City.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        city=self.get_object(pk)
        serializer=CityModelSerializer(city)
        return Response(serializer.data)

    def put(self,request,pk):
        city=self.get_object(pk)
        serializer=CityModelSerializer(instance=city,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        city=self.get_object(pk)
        city.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


