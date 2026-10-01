from django.contrib import admin
from .models import Zayavka
# Register your models here.
admin.site.site_header = "Конференции.РФ | Панель администратора"
admin.site.register(Zayavka)