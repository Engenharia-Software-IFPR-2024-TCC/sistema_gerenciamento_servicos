from rest_framework import serializers
from authentication.models import Role, Usuario, UsuarioRole


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'
        
        
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        
        
class UsuarioRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioRole
        fields = '__all__'
    