from rest_framework import serializers
from useracount.models import Accounts


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Accounts
#         fields = ['id', 'username', 'email']

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = ['username', 'email', 'password','role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validate_data):
        return Accounts.objects.create_user(**validate_data)
     
   
class UserLoginSerializer(serializers.ModelSerializer):
    email= serializers.EmailField(max_length=255)
    class Meta:
        model=Accounts
        fields = ['email','password']
        
        
        def validate_password(self, value):
            if not value:
                raise serializers.ValidationError(_("msgInvalidpassword"))    


class UserprofileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = ['id', 'email','role']     
