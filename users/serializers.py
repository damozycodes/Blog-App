from rest_framework import serializers
from .models import User


class PhoneNumberSerializer(serializers.CharField):
    def validate_phone_number(self, phone_number):
        if len(phone_number) != 11:
            raise serializers.Error(
                "your phone number must not exist 11 digits"
            )
        common_prefix = ["070", "071", "080", "081", "090", "091"]
        if not any(phone_number.startswith(prefix) for prefix in common_prefix):
            raise serializers.Error(
                "Invalid phone Number"
        )
        return phone_number
    

# class ProfileSerializer(serializers.ModelSerializer):
#     phone_number = PhoneNumberSerializer()

#     class meta:
#         model = Profile
#         field = ["User", "phone_number"]

class UserSerializer(serializers.ModelSerializer):
    phone_number = PhoneNumberSerializer()
    
    class meta:
        model = User
        field = "__all__"

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model

