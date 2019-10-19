from django.contrib import admin
from webapp.models import Poll, Choice


class PollAdmin(admin.ModelAdmin):
    list_display = ['pk', 'question', 'created']
    list_display_links = ['pk', 'question']
    exclude = []


admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
