from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegistrationSerializer
from .utils import send_welcome_email
from django.conf import settings

class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # Save the user
            # Send invitation email
            invite_url = f"https://dubai.scaleupconclave.com/signup?email={user.email}"
            send_welcome_email(
            to_email=user.email,
            recipient_name=user.name
            )


            return Response({"message": "Registered successfully and invitation email sent!"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
