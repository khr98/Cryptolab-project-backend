from django.urls import path
from user import views
from .views import ReadDetailQrCode, SignUpView, QRCodeView,ReadQrCode,ReadDetailQrCode,CreateQrCode,DeleteQrCode,DeleteDetailQrCode,UpdateDetailQrCode

urlpatterns = [
    path('signup/', SignUpView.as_view()),
    path('create/', views.CreateQrCode),
    path('read/',views.ReadQrCode),
    path('read/<int:pk>',views.ReadDetailQrCode),
    path('update/',views.UpdateQrCode),
    path('update/<int:pk>',views.UpdateDetailQrCode),
    path('delete/',views.DeleteQrCode),
    path('delete/<int:pk>',views.DeleteDetailQrCode),
    path('location/',QRCodeView.as_view()),
    path('location/<int:pk>',QRCodeView.as_view()),   
]