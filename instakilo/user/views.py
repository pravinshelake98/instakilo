from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from user.serializers import LoginSerializer, RegistrationSerializer




class Login(APIView):
    """This class create for user login purpose"""

    def post(self,request, format=None):
        serializers_class = LoginSerializer
        serializers=serializers_class(data=request.data)
        serializers.is_valid(raise_exception=True)
        return Response(
            data={"Success":True}
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

        register = serializer_class(data=request.data)
        if register.is_valid(raise_exception=True):
            print("valid data", register.validated_data)
            return Response(
                data={"success": True, "data": request.data}, status=status.HTTP_200_OK)
