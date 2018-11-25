from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from main.serializers import CustomerModelSerilizer
from main.models import Customer


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
    def get_object(self, pk):
        try:
            return Customer.objects.get(id=pk)
        except Customer.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        customer=self.get_object(pk)
        serializer=CustomerModelSerilizer(customer)
        return Response(serializer.data)

    def put(self,request,pk):
        customer=self.get_object(pk)
        serializer=CustomerModelSerilizer(instance=customer,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        customer=self.get_object(pk)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


