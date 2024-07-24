from rest_framework.decorators import action
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from authentication.api.serializers import UsuarioSerializer
from rest_framework_simplejwt.tokens import RefreshToken

    
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
        print("Teste")
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            usuario = serializer.save()
            return Response({
                'usuario': serializer.data,
                'message': 'User registered successfully'
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
