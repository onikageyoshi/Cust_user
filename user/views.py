from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from .serializers import UserSerializer, CreateUserSerializer
from .models import User

class UserDetailsView(APIView):
    @swagger_auto_schema(responses={200: UserSerializer})
    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(
                {"error": "User not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = UserSerializer(user)
        return Response(serializer.data)


class CreateUserView(APIView):
    @swagger_auto_schema(
        request_body= CreateUserSerializer,
        operation_description= "create a user"
    )

    def post(self, request):
        serilaizer = CreateUserSerializer(data=request.data)
        if serilaizer.is_valid():
            serilaizer.save()
            return Response(serilaizer.data, status=status.HTTP_201_CREATED)
        return Response(serilaizer.errors, status=status.HTTP_400_BAD_REQUEST)


