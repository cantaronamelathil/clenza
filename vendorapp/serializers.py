from rest_framework import serializers
from useracount.models import Accounts
from .models import Vendor
from django.contrib.auth import authenticate
# class VendorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Vendor
#         fields = ('username', 'email', 'phone_number', 'address', 'firm_name', 'services')

class VendorRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = Vendor
        fields = ('username', 'email', 'phone_number', 'address', 'firm_name', 'services', 'password')
    def create(self, validated_data):
        password = validated_data.pop('password')
        vendor = Vendor.objects.create(**validated_data)
        vendor.set_password(password)
        vendor.save()
        return vendor

class VendorLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    class Meta:
        model = Accounts
        fields = ('email','password')

    # def validate(self, data):
    #     email = data.get("email")
    #     password = data.get("password")

    #     if email and password:
    #         vendor = authenticate(email=email, password=password)
    #         if vendor:
    #             if not vendor.is_vendor:
    #                 msg = "This user is not a vendor"
    #                 raise serializers.ValidationError(msg)
    #         else:
    #             msg = "Unable to log in with provided credentials."
    #             raise serializers.ValidationError(msg)
    #     else:
    #         msg = "Must include email and password."
    #         raise serializers.ValidationError(msg)

    #     data["vendor"] = vendor
        # return data   
        
        
        