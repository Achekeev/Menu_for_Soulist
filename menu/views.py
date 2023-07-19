from rest_framework import generics
from .models import Branch, MenuCategory, MenuItem, MenuPosition, MenuSubItems
from .serializers import (
    BranchSerializer, MenuCategorySerializer,
    MenuItemSerializer, MenuSubItemSerializer, MenuPositionSerializer
)

class BranchListAPIView(generics.ListAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

class BranchRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

class MenuCategoryListAPIView(generics.ListAPIView):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer

class MenuCategoryRetrieveAPIView(generics.RetrieveAPIView):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer

class MenuItemListAPIView(generics.ListAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class MenuItemRetrieveAPIView(generics.RetrieveAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class MenuSubItemRetrieveAPIView(generics.RetrieveAPIView):
    queryset = MenuSubItems.objects.all()
    serializer_class = MenuSubItemSerializer


class MenuSubItemListAPIView(generics.ListAPIView):
    queryset = MenuSubItems.objects.all()
    serializer_class = MenuSubItemSerializer


class MenuPositionListAPIView(generics.ListAPIView):
    queryset = MenuPosition.objects.all()
    serializer_class = MenuPositionSerializer

class MenuPositionRetrieveAPIView(generics.RetrieveAPIView):
    queryset = MenuPosition.objects.all()
    serializer_class = MenuPositionSerializer


