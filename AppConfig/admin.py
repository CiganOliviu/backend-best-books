from django.contrib import admin

from AppConfig.models import Schema, AppLayout


class SchemaAdmin(admin.ModelAdmin):
    list_display = ('name', 'route')


admin.site.register(Schema, SchemaAdmin)
admin.site.register(AppLayout)
