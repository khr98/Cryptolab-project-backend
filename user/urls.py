from django.urls import path, include
# from user import views
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    path('signup/', views.SignUpAPIView.as_view()),
    path('login/',views.LoginAPIView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # path("rest-auth/", include('rest_auth.urls')),
    # path("rest-auth/registration/", include('rest_auth.registration.urls')),
    # path('create/', views.CreateQrCode),
    # path('read/',views.ReadQrCode),
    # path('read/<int:pk>',views.ReadDetailQrCode),
    # path('update/',views.UpdateQrCode),
    # path('update/<int:pk>',views.UpdateDetailQrCode),
    # path('delete/',views.DeleteQrCode),
    # path('delete/<int:pk>',views.DeleteDetailQrCode),
    path('location/',views.QrCodeAPIView.as_view()),
    path('location/<int:pk>',views.QRCodeDetailAPIView.as_view()),   
]