from django.contrib import admin

from ..models import Empresa


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nome',
    ]

    search_fields = [
        'id',
        'nome',
    ]

    # list_filter = [
    #     '
    # ]

    # list_select_related = [
    #     'usuarios'
    # ]

    # autocomplete_fields = [
    #     'usuarios',
    # ]

    filter_horizontal = ['usuarios']
