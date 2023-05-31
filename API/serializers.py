from rest_framework import serializers
from django.contrib.auth import authenticate,login,get_user_model
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from authentication import models


class UserSerializer(serializers.ModelSerializer):
    user = serializers.CharField()
    password = serializers.CharField()
    
    class Meta:
        model = models.CustomUser
        fields = ['user', 'password']
    
    def validate(self, attrs):
        usuario= attrs.get('user')
        senha= attrs.get('password')
        usuario = authenticate(username = usuario, password = senha)
        if usuario is None:
            raise serializers.ValidationError('Credenciais invalidas.')
        
        attrs['usuario'] = usuario
        return attrs 
    

class UserInfo(serializers.ModelSerializer):
    key = serializers.CharField()

    class Meta:
        model = models.CustomUser
        fields = ['key']

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = '__all__'

class signupSerializer(serializers.ModelSerializer):
    usuario = serializers.CharField()
    email = serializers.EmailField()
    senha1 = serializers.CharField()
    senha2 = serializers.CharField()

    class Meta:
        model = models.CustomUser
        fields = ['usuario', 'email', 'senha1','senha2']
