from rest_framework import serializers
from authentication.models import User
from core.models.role import Role
        
class UserSerializer(serializers.ModelSerializer):
    roles = serializers.SlugRelatedField(
        queryset=Role.objects.all(),
        slug_field='id',
        many=True
    )

    class Meta:
        model = User
        fields = ['id', 'email', 'nome', 'senha', 'cpf', 'roles']
        extra_kwargs = {
            'senha': {'write_only': True},
        }

    def create(self, validated_data):
        roles_data = validated_data.pop('roles')
        usuario = User.objects.create(**validated_data)
        usuario.roles.set(roles_data)
        return usuario
