from django.contrib import admin
from .models import Server, Tag, Result, ResultOneMinute, MessageTag, MessageBit, MessageEvent


class ServerAdmin(admin.ModelAdmin):
    list_display = ('name', 'enable',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'enable', 'server_name',)


class ResultAdmin(admin.ModelAdmin):
    list_display = ('tag_name', 'date', 'display_len',)


class ResultOneMinuteAdmin(admin.ModelAdmin):
    list_display = ('tag_name', 'lost_time', 'display_len',)


class MessageTagAdmin(admin.ModelAdmin):
    list_display = ('name', 'enable',)


class MessageBitAdmin(admin.ModelAdmin):
    list_display = ('name', 'text')


class MessageEventAdmin(admin.ModelAdmin):
    list_display = ('text', 'ask_status', 'event_dt', 'ask_dt')


admin.site.register(Server, ServerAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Result, ResultAdmin)
admin.site.register(ResultOneMinute, ResultOneMinuteAdmin)

admin.site.register(MessageTag, MessageTagAdmin)
admin.site.register(MessageBit, MessageBitAdmin)
admin.site.register(MessageEvent, MessageEventAdmin)
