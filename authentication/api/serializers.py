from rest_framework import serializers
from authentication.models import Role, Usuario, UsuarioRole


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'
        
        
class UsuarioSerializer(serializers.ModelSerializer):
    roles = serializers.SlugRelatedField(
        queryset=Role.objects.all(),
        slug_field='id',
        many=True
    )

    class Meta:
        model = Usuario
        fields = ['id', 'email', 'nome', 'senha', 'cpf', 'roles']
        extra_kwargs = {
            'senha': {'write_only': True},
        }

    def create(self, validated_data):
        roles_data = validated_data.pop('roles')
        usuario = Usuario.objects.create(**validated_data)
        usuario.roles.set(roles_data)
        return usuario
        
        
class UsuarioRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioRole
        fields = '__all__'
    