from rest_framework import serializers
from .models import Registration

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'

    def validate_mobile(self, value):
        if len(value) != 10 or not value.isdigit():
            raise serializers.ValidationError("Mobile number must be exactly 10 digits.")
        return value

    def validate(self, data):
        email = data.get('email')
        mobile = data.get('mobile')

        if Registration.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": "Email already registered."})

        if Registration.objects.filter(mobile=mobile).exists():
            raise serializers.ValidationError({"mobile": "Mobile number already registered."})

        return data
