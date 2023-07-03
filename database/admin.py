from django.contrib import admin
from .models import Kit, Modulo, Inversor, Cabo, Estrutura

@admin.register(Kit)
class KitAdmin(admin.ModelAdmin):
    pass

@admin.register(Modulo)
class ModuloAdmin(admin.ModelAdmin):
    pass

@admin.register(Inversor)
class InversorAdmin(admin.ModelAdmin):
    pass

@admin.register(Cabo)
class CaboAdmin(admin.ModelAdmin):
    pass

@admin.register(Estrutura)
class EstruturaAdmin(admin.ModelAdmin):
    pass
# Register your models here.
