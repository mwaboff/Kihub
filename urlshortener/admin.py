from django.contrib import admin

from .models import URL

# Register your models here.

class URLAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['orig_url', 'short_url', 'views']}),
        ("Date Information", {'fields':['creation_date']}),

    ]

    list_display = ('short_url', 'orig_url', 'views', 'creation_date')
    list_filter = ['creation_date']
    search_fields = ['short_url', 'orig_url']

admin.site.register(URL, URLAdmin)