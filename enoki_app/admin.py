from django.contrib import admin

from enoki_app.models import (
    CustomUser
)

# Register your models here.

from django.contrib import admin

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    # Fields are sliced in order to not display password field.
    list_display = [element.name for element in CustomUser._meta.fields[:1] + CustomUser._meta.fields[2:]]
