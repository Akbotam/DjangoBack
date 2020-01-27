from api.models import Company
from django.contrib.auth.models import User
from api.serializers import CompanySerializer2, UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class CompanyList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Company.objects.for_user(self.request.user)

    def get_serializer_class(self):
        return CompanySerializer2

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer2


