from django.db import models


class Empresa(models.Model):

    nome = models.CharField(
        verbose_name='Nome',
        max_length=100,
    )

    proprietario = models.CharField(
        verbose_name='Nome proprietário',
        max_length=100,
    )

    telefone = models.CharField(
        verbose_name='Telefone',
        max_length=20,
        blank=True, null=True
    )

    logo = models.ImageField(
        verbose_name='Logo',
        upload_to='logos',
        blank=True, null=True
    )

    cnpj = models.CharField(
        verbose_name='CNPJ',
        max_length=20,
        unique=True,
        blank=True, null=True
    )

    endereco = models.CharField(
        verbose_name='Endereço',
        max_length=200,
        blank=True, null=True
    )

    data_criacao = models.DateTimeField(
        verbose_name='Data de criação',
        auto_now_add=True
    )

    usuarios = models.ManyToManyField(
        'home.Profile',
        verbose_name='Usuários',
        blank=True, null=True,
        related_name='empresas'
    )
    
    

    def __str__(self):
        '''Método que retorna a representação do objeto como string.'''
        return self.nome

    class Meta:
        '''Sub classe para definir meta atributos da classe principal.'''

        app_label = 'empresa'
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
