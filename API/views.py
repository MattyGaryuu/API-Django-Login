from django.shortcuts import render
from authentication import models as authm
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view
from .serializers import UserSerializer,UserInfo,CustomUserSerializer
import jwt
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your views here.


@api_view(['POST'])
def loginAPI(request):
    Login = UserSerializer(data=request.data)
    Login.is_valid(raise_exception=True)

    usuario = Login.validated_data['usuario']

    token = str(RefreshToken.for_user(usuario).access_token)
    context = {
        'access_token': token,
    }

    return Response(context)

@api_view(['POST'])
def UserAPI(request):
    user = UserInfo(data=request.data)
    user.is_valid(raise_exception=True)
    token = user.validated_data['key']
    print(f'key = {token} secret = {settings.SECRET_KEY}')
    try:
        user_id = jwt.decode(token,settings.SECRET_KEY,algorithms=["HS256"])
        user_obj = CustomUserSerializer(get_user_model().objects.get(ID=user_id['user_id']))
        context = {
                'usuario': user_obj.data
        }
        print(context)
    except:
        context = {
            'error': 'Sessao Finalizada e/ou usuario inexistente'
        }
    return Response(context)

