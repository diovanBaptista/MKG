from django.contrib import admin

from ..models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nome',
    ]

    search_fields = [
        'id',
        'nome',
    ]

    list_filter = [
    ]

    # list_select_related = [
    #     'campos_dos_campos_fk
    # ]

    autocomplete_fields = [
        'user',
    ]
