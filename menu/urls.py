from django.urls import path
from .views import (
    BranchListAPIView, BranchRetrieveAPIView,
    MenuCategoryListAPIView, MenuCategoryRetrieveAPIView,
    MenuItemListAPIView, MenuItemRetrieveAPIView,
    MenuPositionListAPIView, MenuPositionRetrieveAPIView, MenuSubItemRetrieveAPIView, MenuSubItemListAPIView
)

urlpatterns = [
    path('branches/', BranchListAPIView.as_view(), name='branch-list'),
    path('branches/<int:pk>/', BranchRetrieveAPIView.as_view(), name='branch-detail'),
    path('menucategories/', MenuCategoryListAPIView.as_view(), name='menucategory-list'),
    path('menucategories/<int:pk>/', MenuCategoryRetrieveAPIView.as_view(), name='menucategory-detail'),
    path('menuitems/', MenuItemListAPIView.as_view(), name='menuitem-list'),
    path('menuitems/<int:pk>/', MenuItemRetrieveAPIView.as_view(), name='menuitem-detail'),
    path('menupositions/', MenuPositionListAPIView.as_view(), name='menuposition-list'),
    path('menupositions/<int:pk>/', MenuPositionRetrieveAPIView.as_view(), name='menuposition-detail'),
    path('menusubs/<int:pk>/', MenuItemRetrieveAPIView.as_view(), name='MenuSubItem-detail'),
    path('menusubs-list/', MenuSubItemListAPIView.as_view(), name='MenuSubItems-List'),

]
