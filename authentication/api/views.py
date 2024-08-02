import bcrypt
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from authentication.api.serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from authentication.models import User

    
class AutenticacaoView(ViewSet):
    authentication_classes = [JWTAuthentication]

    def list(self, request, *args, **kwargs):
        content = {'message': 'List of items'}
        return Response(content, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        content = {'message': f'Item with id {pk}'}
        return Response(content, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'], url_path='registro')
    def registro(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'user': serializer.data,
                'message': 'User registered successfully'
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    @action(detail=False, methods=['post'], url_path='login')
    def login(self, request, *args, **kwargs):
        email = request.data.get('email')
        senha = request.data.get('senha')
            
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'Credenciais inválidas!'}, status=status.HTTP_401_UNAUTHORIZED)

        if bcrypt.checkpw(senha.encode('utf-8'), user.senha.encode('utf-8')):
            refresh = RefreshToken.for_user(user)
            serializer = UserSerializer(user)
            return Response({
                'user': serializer.data,
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh)
            }, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Credenciais inválidas!'}, status=status.HTTP_401_UNAUTHORIZED)

