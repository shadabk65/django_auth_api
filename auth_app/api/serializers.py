from rest_framework import serializers
from auth_app.models import User

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
