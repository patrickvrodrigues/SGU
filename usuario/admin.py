from django.contrib import admin

from .models import Endereco,Polo,Setor, Usuario, Pasta

admin.site.register(Usuario)

admin.site.register(Endereco)

admin.site.register(Polo)

admin.site.register(Pasta)

class SetorAdmin(admin.ModelAdmin):
    
    list_display = ['setor', 'pasta']

    class Meta:
        model = Setor

admin.site.register(Setor, SetorAdmin)


