from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from accounts.permissions import IsAdmin,IsManager,IsUser


class UserProfileView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated,IsUser]
    
    def get(self,request:Request)-> Response:
        print(request)
        return Response(
            {"message":"salom User"}
        )
        
        
class AdminProfileView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated,IsAdmin]
    
    def get(self,request:Request)-> Response:
        return Response(
            {"message":"salom Admin"}
        )
    
class ManagerProfileView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated,IsManager]
    
    def get(self,request:Request)-> Response:
        return Response(
            {"message":"salom Manager"}
    )


