from django.contrib import admin
from home.models import Cargo, Equipe, Servicos


class ServicoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'icone')
    list_filter = ('titulo', 'descricao', 'icone')
    search_fields = ('titulo', 'descricao', 'icone')
    list_per_page = 10


class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo',)
    list_filter = ('cargo',)
    search_fields = ('cargo',)
    list_per_page = 10


class EquipeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargos', 'bio', 'facebook', 'twitter', 'instagram')
    list_filter = ('nome', 'cargos', 'bio', 'facebook', 'twitter', 'instagram')
    search_fields = ('nome', 'cargos', 'bio', 'facebook', 'twitter', 'instagram')
    list_per_page = 10


admin.site.register(Servicos, ServicoAdmin)
admin.site.register(Equipe, EquipeAdmin)
admin.site.register(Cargo, CargoAdmin)
