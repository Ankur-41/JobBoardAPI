from rest_framework import serializers
from .models import Company,Job,Application

class CompanySeriallizer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
        read_only_fields = ['user']

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'
        read_only_fields = ['posted_date','company']

class ApplicationSerializer(serializers.ModelSerializer):
    job_details = JobSerializer(source='job',read_only=True)
    class Meta:
        model = Application
        fields = '__all__'
        read_only_fields = ['user','applied_date']


