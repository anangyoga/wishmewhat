from django.contrib import admin
from .models import Wishes

# Register your models here.
class WishesAdmin(admin.ModelAdmin):
    list_display = ("text", "created_at")

admin.site.register(Wishes, WishesAdmin)
