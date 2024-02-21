from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from user.serializers import LoginSerializer


class Login(APIView):

    def post(self,request, format=None):
        serializers_class = LoginSerializer
        serializers=serializers_class(data=request.data)
        serializers.is_valid(raise_exception=True)
        return Response(
            data={"Success":True}
        )
    

class Registration(APIView):

    def post(self,request, format=None):
        serializers_class = RegistrationSerializer
        serializers=serializers_class(data=request.data)
        serializers.is_valid(raise_exception=True)
        return Response(
            data={"Success":True}
        )
