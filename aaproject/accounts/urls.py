from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

from rest_framework_simplejwt import views as jwt_views
from .views import ProtectedView  

urlpatterns = [
    path('', views.home, name='home'),  # URL pattern for the empty path
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    
    #jwt token
    path('accounts/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('accounts/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('accounts/protected/', ProtectedView.as_view(), name='protected'),
]