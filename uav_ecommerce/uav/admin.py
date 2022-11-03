from django.contrib import admin
from .models import Uav, Category
from django.utils.safestring import mark_safe

class uavAdmin(admin.ModelAdmin):
    list_display = ("model","is_active","is_home","slug",)
    list_editable = ("is_active","is_home",)
    search_fields = ("model","description")
    readonly_fields = ("slug",)
    list_filter = ("is_active","is_home","category",)

    def selected_category(self, obj):
        html = "<ul>"

        for category in obj.Category.all():
            html += "<li>" + category.name + "</li>"

        html += "</ul>"
        return mark_safe(html)
    

admin.site.register(Uav, uavAdmin)
admin.site.register(Category)
