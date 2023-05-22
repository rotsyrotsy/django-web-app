from django.contrib import admin

from listings.models import Band
from listings.models import Song

class BandAdmin(admin.ModelAdmin):
    list_display = ('name','year_formed','genre')

class SongAdmin(admin.ModelAdmin):
    list_display = ('title','band')

admin.site.register(Band, BandAdmin)
admin.site.register(Song, SongAdmin)
