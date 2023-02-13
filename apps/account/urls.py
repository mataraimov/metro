from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from .views import MyObtainPairView,RegisterView
urlpatterns = [
    path('token/',MyObtainPairView.as_view(),name='token'),
    path('token/refresh',TokenRefreshView.as_view(),name='token_refresh'),
    path('register/',RegisterView.as_view(),name='register'),
]
