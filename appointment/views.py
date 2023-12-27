from rest_framework.views import APIView
from .serializers import AppointmentSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError


class AppointmentView(APIView):
    @classmethod
    def post(cls, request):
        data = request.data
        print(data)
        serializer = AppointmentSerializer(data=data)
        try:
            if serializer.is_valid(raise_exception=True):
                serializer.make_appointment(data)
                return Response(status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)

