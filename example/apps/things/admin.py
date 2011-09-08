from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from example.apps.things.models import Thing


class ThingAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'image', 'description'),
        }),
        (_(u'Dates'), {
            'fields': ('created', 'modified'),
            'classes': ('collapse', ),
        }),
    )
    list_display = ('name', 'slug')
    list_filter = ('created', 'modified')
    prepopulated_fields = {'slug': ('name', )}
    readonly_fields = ('created', 'modified')
    search_fields = ('name', 'slug')


admin.site.register(Thing, ThingAdmin)
