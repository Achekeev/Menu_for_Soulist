from rest_framework import serializers
from .models import Branch, MenuCategory, MenuItem, MenuPosition, MenuSubItems


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'


class MenuSubItemSerializer(serializers.ModelSerializer):
    menuitems = MenuItemSerializer(many=True, read_only=True)

    class Meta:
        model = MenuSubItems
        fields = ('id', 'title', 'menuitems')


class MenuItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MenuItem
        fields = '__all__'


class MenuPositionSerializer(serializers.ModelSerializer):
    menusubitems = MenuSubItemSerializer(many=True, read_only=True)
    class Meta:
        model = MenuPosition
        fields = ('id', 'name', 'weight', 'price', 'picture', 'menusubitems')


class MenuCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = MenuCategory
        fields = '__all__'
