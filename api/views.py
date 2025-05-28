from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegistrationSerializer
from .utils import send_welcome_email  # Import your helper function

class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # Save the user
            # Send invitation email
            invite_url = f"https://your-frontend.com/signup?email={user.email}"
            send_welcome_email(
                to_email=user.email,
                inviter_name="Admin",  # You can replace this with request.user.username if user is logged in
                invite_url=invite_url
            )
            return Response({"message": "Registered successfully and invitation email sent!"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
