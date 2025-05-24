from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegistrantSerializer

class RegisterView(APIView):
    def post(self, request):
        serializer = RegistrantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Registered successfully"}, status=status.HTTP_201_CREATED)

        # Collect the first error field and its message
        first_error = next(iter(serializer.errors.items()))
        field, errors = first_error
        return Response({"message": f"{field.capitalize()}: {errors[0]}"}, status=status.HTTP_400_BAD_REQUEST)
