from rest_framework import serializers
from .models import Branch, MenuCategory, MenuItem, MenuPosition, MenuSubItems


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'


class MenuPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuPosition
        fields = '__all__'
        depth = 4


class MenuSubItemSerializer(serializers.ModelSerializer):
    positions = MenuPositionSerializer(many=True, read_only=True)

    class Meta:
        model = MenuSubItems
        fields = ('id', 'title', 'positions')


class MenuCategorySerializer(serializers.ModelSerializer):
    menusubitems = MenuSubItemSerializer(many=True, read_only=True)


    class Meta:
        model = MenuCategory
        fields = ('id', 'title', 'menusubitems')


class BranchSerializer(serializers.ModelSerializer):
    categories = MenuCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Branch
        fields = '__all__'



