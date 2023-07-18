from django.contrib import admin
from .models import Branch, MenuCategory, MenuItem, MenuPosition, MenuSubItems


admin.site.register(Branch)
admin.site.register(MenuCategory)


class MenuPositionInline(admin.StackedInline):
    model = MenuPosition

# class MenuSubItemInline(admin.StackedInline):
#     model = MenuSubItems

class MenuSubItemsAdmin(admin.ModelAdmin):
    inlines = [MenuPositionInline,]


class MenuItemAdmin(admin.ModelAdmin):
    inlines = [MenuPositionInline,]


admin.site.register(MenuSubItems, MenuSubItemsAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(MenuPosition)