# Create your views here.
"""temporary view system we view it later
"""
from django.contrib.auth import authenticate
from django.db import IntegrityError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user.models import UserModel


from user.serializers import LoginSerializer
from user.serializers import RegistrationSerializer


class Login(APIView):
    """this class id for the login page"""

    def post(self, request):
        """post function for the class login

        Args:
            request (type): description
            format (type, optional): description. Defaults to None.

        Returns:
            type: description
        """

        serializer_class = LoginSerializer
        print(request.data)

        serial = serializer_class(data=request.data)

        if serial.is_valid(raise_exception=True):
            print("valid data", serial.validated_data)

        try:
            user = authenticate(
                username=serial.validated_data.get("username"),
                password=serial.validated_data.get("password"),
            )
            print(user)
            if user is not None:
                return Response(
                    data={"success": True, "data": request.data},
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    data={
                        "success": False,
                        "message": "username and password does not match",
                    },
                    status=status.HTTP_200_OK,
                )

        except ValueError:
            return Response(
                data={
                    "success": False,
                    "error": "username and password odes not matched",
                }
            )    


class RegistrationView(APIView):
    """this class id for the login page"""

    def post(self, request):
        """post function for the class login

        Args:
            request (type): description
            format (type, optional): description. Defaults to None.

        Returns:
            type: description
        """

        serializer_class = RegistrationSerializer
        print(request.data)

        serializer = serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print("valid data", serializer.validated_data)
            try:
                user_obj = UserModel.objects.create(
                    username=serializer.validated_data.get("username"),
                    first_name=serializer.validated_data.get("firstname"),
                    last_name=serializer.validated_data.get("lastname"),
                    email=serializer.validated_data.get("emailid"),
                )
                user_obj.set_password(serializer.validated_data.get("password"))
                user_obj.save()

                return Response(
                    data={
                        "success": True,
                        "username": user_obj.username,
                        "email": user_obj.email,
                    },
                    status=status.HTTP_200_OK,
                )

            except IntegrityError as e:
                return Response(
                    data={
                        "success": False,
                        "message": str(e)
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
        