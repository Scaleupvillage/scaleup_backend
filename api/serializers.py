from rest_framework import serializers
from .models import Registrant

class RegistrantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registrant
        fields = '__all__'

    def validate_email(self, value):
        if Registrant.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already registered.")
        return value

    def validate_mobile(self, value):
        if Registrant.objects.filter(mobile=value).exists():
            raise serializers.ValidationError("This mobile number is already registered.")
        return value
