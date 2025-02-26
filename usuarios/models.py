from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(models.Model):
    # Your model fields here
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    # ... other fields

    def __str__(self):
        return self.nome # or a relevant field.
class CustomUser(AbstractUser):
    """
    Modelo de usuário personalizado que estende AbstractUser.
    Você pode adicionar campos personalizados aqui.
    """
    # Exemplo de campo personalizado (opcional):
    # idade = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        swappable = 'AUTH_USER_MODEL'