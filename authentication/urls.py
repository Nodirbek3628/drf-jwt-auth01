from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from .views import (AdminProfileView,UserProfileView,ManagerProfileView,
                    GoogleLoginView,GoogleCallbackView)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/',TokenVerifyView.as_view(), name='token_verify'),
    path('userprofile/', UserProfileView.as_view(), name='profile'),
    path('adminprofile/', AdminProfileView.as_view(), name='profile'),
    path('managerprofile/', ManagerProfileView.as_view(), name='profile'),
    
    path('google/login/',GoogleLoginView.as_view(),name='google_login'),
    path('google/callback/',GoogleCallbackView.as_view(),name='google_callback'),
    
]
