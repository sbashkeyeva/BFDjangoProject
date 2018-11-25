from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from main.serializers import FlowerModelSerializer
from main.models import Flower


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
    def get_object(self, pk):
        try:
            return Flower.objects.get(id=pk)
        except Flower.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        flower=self.get_object(pk)
        serializer=FlowerModelSerializer(flower)
        return Response(serializer.data)

    def put(self,request,pk):
        flower=self.get_object(pk)
        serializer=FlowerModelSerializer(instance=flower,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        flower=self.get_object(pk)
        flower.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


