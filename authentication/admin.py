from django.contrib import admin
from .models import Role, Usuario, UsuarioRole, Perfil


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao')
    

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('id', 'rua', 'numero', 'cep', 'cidade', 'estado')


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'nome', 'criado_em', 'cpf', 'senha')
    readonly_fields = ('id', 'criado_em')


@admin.register(UsuarioRole)
class UsuarioRoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_usuario_nome', 'get_role_nome')

    def get_usuario_nome(self, obj):
        return obj.usuario.nome
    
    get_usuario_nome.short_description = 'Usuário'

    def get_role_nome(self, obj):
        return obj.role.nome
    
    get_role_nome.short_description = 'Role'