from django.urls import path, include
# from user import views
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

urlpatterns = [
    path('signup/', views.SignUpAPIView.as_view()),
    path('login/',views.LoginAPIView.as_view()),
    path('token/',TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('token/refresh/',TokenRefreshView.as_view(), name='token_refresh'),
    # path("rest-auth/", include('rest_auth.urls')),
    # path("rest-auth/registration/", include('rest_auth.registration.urls')),
    path('locations/',views.QrCodeAPIView.as_view()),
    path('locations/<int:pk>',views.QRCodeDetailAPIView.as_view()),   
]