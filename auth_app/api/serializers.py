from rest_framework import serializers
from auth_app.models import User
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator

class UserRegistrationSerializer(serializers.ModelSerializer):
	password2 = serializers.CharField(style = {'input_type':'password'}, write_only = True)
	class Meta:
		model = User
		fields = ['email', 'name', 'password', 'password2']
		extra_kwargs = {
		  'password' : {'write_only':True}
		}

	def validate(self, value):
		password = value.get('password')
		password2 = value.get('password2')
		if password != password2:
			raise serializers.ValidationError("password did not match")
		return value
	def create(self, validate_data):
		return User.objects.create_user(**validate_data)

class UserLoginSerializer(serializers.ModelSerializer):
	email = serializers.EmailField(max_length=255)
	class Meta:
		model = User
		fields = ['email', 'password']

class UserProfileViewSerializer(serializers.ModelSerializer):
	class Meta:
		model=User
		fields = ['id','email', 'name']

class UserChangePasswordSerializer(serializers.Serializer):

	password = serializers.CharField(style = {'input_type':'password'}, write_only = True, max_length=255)
	password2 = serializers.CharField(style = {'input_type':'password'}, write_only=True, max_length=255)

	class Meta:
		fields  = ['password', 'password2']

	def validate(self, value):
		password = value.get('password')
		password2 = value.get('password2')
		user = self.context.get('user')
		if password != password2:
			raise serializers.ValidationError("password did not match")
		user.set_password(password)
		user.save()
		return value

class SendpasswordResetEmailSerializer(serializers.Serializer):
	email = serializers.EmailField(max_length=255)
	class Meta:
		fields = ['email']

	def validate(self, value):
		email = value.get('email')
		if User.objects.filter(email=email).exists():
			user = User.objects.get(email=email)
			uid = urlsafe_base64_encode(force_bytes(user.id))
			token = PasswordResetTokenGenerator().make_token(user)
			link = 'http://localhost:3000/api/reset/'+uid+'/'+token
			print("uel", link)
			return value
		else:
			raise serializers.ValidationError('you are not registered')

class UserResetPasswordSerializer(serializers.Serializer):
	password = serializers.CharField(style = {'input_type':'password'}, write_only = True, max_length=255)
	password2 = serializers.CharField(style = {'input_type':'password'}, write_only=True, max_length=255)

	class Meta:
		fields  = ['password', 'password2']

	def validate(self, value):
		password = value.get('password')
		password2 = value.get('password2')
		uid = self.context.get('uid')
		token = self.context.get('token')
		if password != password2:
			raise serializers.ValidationError("password did not match")
		id = smart_str(urlsafe_base64_decode(uid))
		user = User.objects.get(id=id)
		if not PasswordResetTokenGenerator().check_token(user,token):
			raise ValueError('token is not valid')
		user.set_password(password)
		user.save()
		return value
