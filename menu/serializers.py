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
    menu_item = serializers.SerializerMethodField()

    class Meta:
        model = MenuSubItems
        fields = '__all__'
        depth = 1


class MenuPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuPosition
        fields = '__all__'
