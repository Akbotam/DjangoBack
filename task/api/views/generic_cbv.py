from api.models import Company, Review
from api.serializers import CompanySerializer2, ReviewSerializer
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
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Company.objects.for_user(self.request.user)

    def get_serializer_class(self):
        return CompanySerializer2

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ReviewList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Review.objects.for_user(self.request.user)

    def get_serializer_class(self):
        return ReviewSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


