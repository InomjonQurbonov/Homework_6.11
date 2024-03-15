from django.contrib import admin

from .models import Pupil

class PupilAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    search_fields = ('name',)
    list_filter = ('all_points',)


admin.site.register(Pupil, PupilAdmin)
