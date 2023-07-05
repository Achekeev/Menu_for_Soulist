from rest_framework import serializers
from .models import Branch, MenuCategory, MenuItem, MenuPosition, MenuSubItems


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'



class MenuCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = MenuCategory
        fields = '__all__'
        depth = 1


class MenuItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MenuItem
        fields = '__all__'
        depth = 1

class MenuSubItemSerializer(serializers.ModelSerializer):
    menuitems = MenuItemSerializer(many=True, read_only=True)

    class Meta:
        model = MenuSubItems
        fields = ('id', 'title', 'menuitems')
        depth = 1




class MenuPositionSerializer(serializers.ModelSerializer):
    menusubitems = MenuSubItemSerializer(many=True, read_only=True)
    class Meta:
        model = MenuPosition
        fields = ('id', 'name', 'weight', 'price', 'picture', 'menusubitems')
        depth = 1
