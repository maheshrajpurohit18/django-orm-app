from django.db import models
from django.contrib import admin

class Database(models.Model):
    registration_number_primary_key = models.CharField(max_length=30, primary_key=True,unique=True)
    model = models.CharField(max_length=30)
    company = models.CharField(max_length=20)
    price = models. IntegerField(max_length=20)
    year_of_manufacture = models.IntegerField()
    cc = models.IntegerField()

class Admin(admin.ModelAdmin):
    list_display = ('company', 'model', 'year_of_manufacture', 'cc', 'price','registration_number_primary_key')