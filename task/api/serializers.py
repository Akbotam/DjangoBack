from rest_framework import serializers
from api.models import Company, Reviewer
from django.contrib.auth.models import User


class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)

    def create(self, validated_data):
        company = Company(**validated_data)
        company.save()
        return company

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class CompanySerializer2(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)

    class Meta:
        model = Company
        fields = ('id', 'name')

class ReviewerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = Reviewer
        fields = ('id', 'name', 'email')

class ReviewSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True)
    summary = serializers.CharField(required=True)
    publication_date = serializers.DateTimeField()
    company = CompanySerializer2()
    reviewer = ReviewerSerializer()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')
