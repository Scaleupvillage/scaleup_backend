from rest_framework import serializers
from .models import Registration

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        # Exclude unique_id and submitted_at from input; they are set automatically
        exclude = ['unique_id', 'submitted_at']

    def validate_mobile(self, value):
        if not (7 <= len(value) <= 15) or not value.isdigit():
            raise serializers.ValidationError("Invalid mobile number.")
        return value

    def validate_email(self, value):
        value = value.lower()
        if Registration.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already registered.")
        return value

    def validate(self, data):
        mobile = data.get('mobile')
        if mobile and Registration.objects.filter(mobile=mobile).exists():
            raise serializers.ValidationError({"mobile": "Mobile number already registered."})
        return data
