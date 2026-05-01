from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile



class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    is_company = serializers.BooleanField(default=False)

    class Meta:
        model = User
        fields = ['username','email','password','is_company']

    def create(self, validated_data):
        is_company  = validated_data.pop('is_company',False)
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        Profile.objects.create(user=user,is_company=is_company)
        return user



