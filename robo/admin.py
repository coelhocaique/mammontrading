from django.contrib import admin
from .models import Robo, RoboComprado

# Register your models here.

class RoboAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nome',)}

admin.site.register(Robo, RoboAdmin)
admin.site.register(RoboComprado)
