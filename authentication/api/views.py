from rest_framework.decorators import action
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status
from authentication.api.serializers import UsuarioSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class AutenticacaoView(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
    
    
    @action(detail=False, methods=['post'], url_path='registro')
    def registro(self, request):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            usuario = serializer.save()
            refresh_token = RefreshToken.for_user(usuario)
            return Response({
                'usuario': serializer.data,
                'refresh_token': str(refresh_token),
                'access_token': str(refresh_token.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)