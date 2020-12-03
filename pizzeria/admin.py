from django.contrib import admin
from .models import Pizza, Topping, Size
# Register your models here.

admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Size)