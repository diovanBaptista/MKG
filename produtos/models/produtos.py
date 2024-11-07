from django.db import models


class Produto(models.Model):

    nome = models.CharField(
        verbose_name='Nome',
        max_length=100,
    )

    preco = models.DecimalField(
        verbose_name='Preço',
        max_digits=10,
        decimal_places=2,
    )

    valor_promocional = models.DecimalField(
        verbose_name='Valor promocional',
        max_digits=10,
        decimal_places=2,
    )

    imagem = models.ImageField(
        verbose_name='Imagem',
        upload_to='produto_imagens',
        blank=True, null=True,
    )

    categoria = models.ForeignKey(
        'produtos.Categoria',
        verbose_name='Categoria',
        on_delete=models.CASCADE,
        blank=True, null=True,
    )

    empresa = models.ForeignKey(
        'empresa.Empresa',
        verbose_name='Empresa',
        on_delete=models.CASCADE,
        blank=True, null=True,
    )

    def __str__(self):
        '''Método que retorna a representação do objeto como string.'''
        return self.nome

    class Meta:
        '''Sub classe para definir meta atributos da classe principal.'''

        app_label = 'produtos'
        verbose_name = 'produto'
        verbose_name_plural = 'produtos'
