from rest_framework import serializers
from django.contrib.auth.models import User


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20, min_length=5)
    password = serializers.CharField(max_length=8, min_length=4)


class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=8, min_length=4)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'confirm_password')

    def save(self):
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']
        email = self.validated_data['email']

        if confirm_password != password:
            data = {
                "status": "False",
                "message": "Passwords don't matched!!!"
            }
            return data

        if User.objects.filter(email=email).exists():
            data = {
                "status": "False",
                "message": "Email is available in the database"
            }
            return data

        account = User(email=email, username=self.validated_data['username'])
        account.set_password(password)
        account.save()
        return account
