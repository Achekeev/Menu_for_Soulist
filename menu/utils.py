from .models import MenuCategory

def get_child_categories(category):
    child_categories = MenuCategory.objects.filter(parent=category)
    return child_categories