from api.models import Company
from api.serializers import CompanySerializer2
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CompanyList(APIView):
    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer2(companies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = CompanySerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CompanyDetail(APIView):

    def get_object(self, pk):
        try:
            return Company.objects.get(id=pk)
        except Company.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        company = self.get_object(pk)
        serializer = CompanySerializer2(company)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self, request, pk):
        company = self.get_object(pk)
        serializer = CompanySerializer2(instance=company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def delete(self, request, pk):
        company = self.get_object(pk)
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
