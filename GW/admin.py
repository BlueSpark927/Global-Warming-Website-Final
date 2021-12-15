from django.contrib import admin
from django.contrib.admin.decorators import register
# Register your models here.
from .models import Months, Year


admin.site.register(Months)
admin.site.register(Year)