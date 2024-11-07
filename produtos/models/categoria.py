from django.db import models


class Categoria(models.Model):
    
    nome = models.CharField(
        verbose_name='Nome',
        max_length=100,
    )

    def __str__(self):
        '''Método que retorna a representação do objeto como string.'''
        return self.nome

    class Meta:
        '''Sub classe para definir meta atributos da classe principal.'''

        app_label = 'produtos'
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
