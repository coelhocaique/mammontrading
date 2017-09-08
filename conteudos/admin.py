from django.contrib import admin
from django.db import models
from django.forms import Textarea

from .models import Artigo, Video

# Register your models here.

admin.site.register(Artigo)
admin.site.register(Video)

