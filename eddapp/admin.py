from django.contrib import admin
from .models import *


@admin.register(PelamarKerja)
class PelamarKerjaAdmin(admin.ModelAdmin):
    pass


@admin.register(PemberiKerja)
class PemberiKerjaAdmin(admin.ModelAdmin):
    pass


@admin.register(Pekerjaan)
class PekerjaanAdmin(admin.ModelAdmin):
    pass


@admin.register(PekerjaanPelamarKerja)
class PekerjaanPelamarKerjaAdmin(admin.ModelAdmin):
    pass
