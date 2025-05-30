from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegistrationSerializer
from .utils import send_welcome_email

class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Build invite URL dynamically
            invite_url = request.build_absolute_uri(f"/signup?email={user.email}")

            try:
                send_welcome_email(
                    send_welcome_email(
                    to_email=user.email,
                    recipient_name=user.name,
                    reg_id=user.unique_id  # or whatever your prebooking/registration ID is
)

                )
            except Exception as e:
                # Log error or handle failure gracefully
                print(f"Failed to send welcome email: {e}")

            return Response({
                "message": "Registered successfully and invitation email sent!",
                "unique_id": user.unique_id
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
