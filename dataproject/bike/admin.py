from re import A
from django.contrib import admin
from .models import Database,Admin
# Register your models here.

admin.site.register(Database,Admin)
