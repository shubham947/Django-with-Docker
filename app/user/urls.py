"""
URL mappings for User APIs
"""
from django.urls import path
from user import views
from rest_framework_simplejwt import views as jwt_views

app_name = 'user'

urlpatterns = [
    path('create/', view=views.CreateUserView.as_view(), name='create'),
    path('account/', view=views.ManageUserView.as_view(), name='account'),
    path('token/', view=jwt_views.TokenObtainPairView.as_view(),
         name='token-obtain-pair'),
    path('token/refresh', view=jwt_views.TokenRefreshView.as_view(),
         name='token-refresh'),
]
