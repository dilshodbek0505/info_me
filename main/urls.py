from django.urls import path

from .views import home, qr_code

urlpatterns = [
    path('<str:username>/', home, name='home'),
    path('qr_code/<str:username>/', qr_code, name='qr_code'),
]
