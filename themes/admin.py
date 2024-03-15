from django.contrib import admin

from themes.models import Themes

class ThemesAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    search_fields = ('title',)


admin.site.register(Themes, ThemesAdmin)
