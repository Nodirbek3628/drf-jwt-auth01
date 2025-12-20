import requests
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import AccessToken,RefreshToken

from accounts.permissions import IsAdmin,IsManager,IsUser
from accounts.models import CustomUser


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



class GoogleLoginView(APIView):
    
    def post(self,request:Request)->Response:
        
        url = f'https://accounts.google.com/o/oauth2/v2/auth?'\
                f'client_id={settings.GOOGLE_CLIENT_ID}&'\
                f'redirect_uri={settings.GOOGLE_REDIRECT_URL}&'\
                'response_type=code&'\
                'scope=email%20profile'

                
        return Response(
            {
                "message":"google orqali aut qilishg uchun link",
                "Google link":url
            }
        )
                    


class GoogleCallbackView(APIView):
    
    def get(self,request:Request)->Response:
        
        code = request.query_params.get('code')
        
        if code is None:
            return Response({'errors':'code is required.'},status=status.HTTP_400_BAD_REQUEST)
        
        data = {
            'client_id':settings.GOOGLE_CLIENT_ID,
            'client_secret':settings.GOOGLE_SECRET,
            'grant_type':'authorization_code',
            'redirect_uri':settings.GOOGLE_REDIRECT_URL,
            'code':code 
        }
        
        
        access_token = requests.post(settings.GOOGLE_TOKEN_URL,data=data).json()['access_token']
        
        user = requests.get(settings.GOOGLE_USER_INFO_URL,headers={'Authorization':f'Bearer {access_token}'}).json()
        
        user,creted = CustomUser.objects.get_or_create(
            username = user['email'],
            defaults={
                'email':user['email'],
                'first_name':user.get('given_name',''),
                'last_name': user.get('family_name',''),
                'profile_picture': user.get('picture','')
            }
        )
        
        
        tokens = {
            'access' : str(AccessToken.for_user(user)),
            'refresh': str(RefreshToken.for_user(user))
        }
        
        return Response({'Tokens': tokens })