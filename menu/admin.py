from django.contrib import admin
from .models import Branch, MenuCategory, MenuItem, MenuPosition, MenuSubItems


admin.site.register(Branch)
admin.site.register(MenuCategory)
admin.site.register(MenuItem)


class MenuPositionInline(admin.StackedInline):
    model = MenuPosition


class MenuSubItemsAdmin(admin.ModelAdmin):
    inlines = [MenuPositionInline,]


admin.site.register(MenuSubItems, MenuSubItemsAdmin)
