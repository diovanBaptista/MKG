from django.contrib import admin

from ..models import Produto


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nome',
    ]

    search_fields = [
        'id',
        'nome',
    ]

    list_filter = [
        'categoria',
    ]


    autocomplete_fields = [
        'categoria',
        'empresa',
    ]
