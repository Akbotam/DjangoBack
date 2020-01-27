from api.models import Company
from django.contrib.auth.models import User
from api.serializers import CompanySerializer2, UserSerializer
from rest_framework import generics

class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer2

class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer2

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

