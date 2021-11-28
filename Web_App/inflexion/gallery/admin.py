from django.contrib import admin

# Register your models here.
from .models import Images,UserReg

admin.site.register(Images)
admin.site.register(UserReg)