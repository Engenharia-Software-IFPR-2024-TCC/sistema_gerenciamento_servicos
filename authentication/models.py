import uuid
import bcrypt
from django.db import models


class Role(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    descricao = models.TextField()

    def __str__(self):
        return self.nome


class Perfil(models.Model):
    rua = models.CharField(max_length=255)
    numero = models.CharField(max_length=6)
    cep = models.CharField(max_length=10)
    estado = models.CharField(max_length=100)
    cidade = models.CharField(max_length=120)
    foto_perfil = models.TextField()
    
    def __str__(self):
        return f"{self.rua}, {self.numero}, {self.cep}, {self.cidade} - {self.estado}"
    

class Usuario(models.Model):
    id = models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
            editable=False
    )
    email = models.EmailField(
        verbose_name='Endereço de e-mail', max_length=255, unique=True
    )
    nome = models.CharField(max_length=155)
    senha = models.CharField(max_length=255)
    criado_em = models.DateTimeField(auto_now_add=True)
    cpf = models.CharField(max_length=11, unique=True)
    roles = models.ManyToManyField(Role, through='UsuarioRole')
    perfil = models.ForeignKey(
        Perfil, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        if self.senha:
            senha_bytes = self.senha.encode('utf-8')
            salt = bcrypt.gensalt()
            hashed_senha = bcrypt.hashpw(senha_bytes, salt)
            self.senha = hashed_senha.decode('utf-8')
        super().save(*args, **kwargs)
    
    
class UsuarioRole(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.usuario.email} - {self.role.nome}"