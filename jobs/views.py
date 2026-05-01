from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from .models import Company,Job,Application
from rest_framework import viewsets,permissions
from rest_framework.exceptions import ValidationError
from .serializers import CompanySeriallizer,JobSerializer,ApplicationSerializer

# Create your views here.
class IsCompanyUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return hasattr(request.user, 'profile') and request.user.profile.is_company

class IsCompanyOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user
    
class IsJobseeker(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return hasattr(request.user,'profile') and not request.user.profile.is_company


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySeriallizer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsCompanyUser]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsCompanyOwner]
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['location', 'job_type']
    search_fields = ['title', 'description']
    ordering_fields = ['salary', 'posted_date']

    def perform_create(self, serializer):
        company = Company.objects.filter(user=self.request.user).first()

        if not company:
            raise ValidationError("No company found for this user")

        serializer.save(company=company)

class ApplicationViewSet(viewsets.ModelViewSet):
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated,IsJobseeker]

    def get_queryset(self):
        return Application.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)



