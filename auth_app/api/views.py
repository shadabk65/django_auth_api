from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from auth_app.api.serializers import UserRegistrationSerializer, UserLoginSerializer, UserProfileViewSerializer, UserChangePasswordSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserRegistrationView(APIView):
	def post(self, request, format=None):
		serializer = UserRegistrationSerializer(data=request.data)
		if serializer.is_valid(raise_exception=True	):
			user = serializer.save()
			token = get_tokens_for_user(user)
			return Response({'token':token,'msg':'registration successfull'})
		return Response({'msg':'registration not successfull'})


class UserLoginView(APIView):
	def post(self, request,format=None):
		serializer = UserLoginSerializer(data=request.data)
		if serializer.is_valid(raise_exception=True):
			email = serializer.data.get('email')
			password = serializer.data.get('password')
			user = authenticate(email=email, password=password)
			if user is not None:
				token = get_tokens_for_user(user)
				return Response({'token':token, 'msg':'Login successfull'})
			else:
				return Response({'msg':'Login not successfull'})

class UserProfileView(APIView):
	permission_classes = [IsAuthenticated]
	def get(self, request, format=None):
		serializer = UserProfileViewSerializer(request.user)
		return Response(serializer.data)

class UserChangePasswordView(APIView):
	permission_classes = [IsAuthenticated]
	def post(self, request, format=None):
		serializer = UserChangePasswordSerializer(data= request.data, context={'user':request.user})
		if serializer.is_valid(raise_exception=True):
			return Response({'msg':'change password successfull'})
