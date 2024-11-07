from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):

    nome = models.CharField(
        verbose_name='Nome',
        max_length=100,
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
    )

    telefone = models.CharField(
        verbose_name='Telefone',
        max_length=20,
    )

    endereco = models.CharField(
        verbose_name='Endereço',
        max_length=200,
    )

    data_nascimento = models.DateField(
        verbose_name='Data de Nascimento',
    )

    cpf = models.CharField(
        verbose_name='CPF',
        max_length=15,
    )

    data_criacao = models.DateTimeField(
        verbose_name='Data de criação',
        auto_now_add=True
    )



    def __str__(self):
        '''Método que retorna a representação do objeto como string.'''
        return self.nome

    class Meta:
        '''Sub classe para definir meta atributos da classe principal.'''

        app_label = 'home'
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
