from django.contrib import admin
from .models import Branch, MenuCategory, MenuItem, MenuPosition, MenuSubItems


admin.site.register(Branch)
admin.site.register(MenuCategory)
admin.site.register(MenuItem)
admin.site.register(MenuPosition)
admin.site.register(MenuSubItems)