from django.urls import path
from .views      import SignUpView, QRCodeView

urlpatterns = [
    path('signup/', SignUpView.as_view()),
    path('location/',QRCodeView.as_view()),
    path('location/<int:pk>',QRCodeView.as_view()),
]