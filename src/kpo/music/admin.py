from django.contrib import admin

from .models import Concert, Song, Part, File

# Register your models here.
admin.site.register(Concert)
admin.site.register(Song)
admin.site.register(Part)
admin.site.register(File)