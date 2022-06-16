from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from auth_app.api.views import UserRegistrationView, UserLoginView, UserProfileView, UserChangePasswordView, SendpasswordResetEmailView, UserResetPasswordView


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('registration/', UserRegistrationView.as_view(), name='user_registration'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('change_password/', UserChangePasswordView.as_view(), name='change-password'),
    path('send_email_reset_password/', SendpasswordResetEmailView.as_view(), name='send_email_reset_password'),
    path('reset_password/<uid>/<token>/', UserResetPasswordView.as_view(), name='reset_password'),

]