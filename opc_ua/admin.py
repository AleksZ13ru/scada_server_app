from django.contrib import admin
from .models import Server, Tag, Result


class ServerAdmin(admin.ModelAdmin):
    list_display = ('name', 'enable',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'enable', 'server_name',)


class ResultAdmin(admin.ModelAdmin):
    list_display = ('tag_name', 'date', 'display_len',)


admin.site.register(Server, ServerAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Result, ResultAdmin)
