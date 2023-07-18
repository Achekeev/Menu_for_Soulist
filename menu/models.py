from django.db import models


class Branch(models.Model):
    title = models.CharField(max_length=100)


    class Meta:
        verbose_name = 'Филиал'
        verbose_name_plural = 'Филиалы'

    def __str__(self):
        return self.title


class MenuCategory(models.Model):
    title = models.CharField(max_length=100)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.title


class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class MenuSubItems(models.Model):
    title = models.CharField(max_length=255)
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='menuitems')

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегорий'


    def __str__(self):
        return self.title


class MenuPosition(models.Model):
    name = models.CharField(max_length=100)
    weight = models.CharField(max_length=255, blank=True, null=True)
    price = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='menu_pictures/', blank=True, null=True)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='menuitems_positions')
    menu_sub_item = models.ForeignKey(MenuSubItems, on_delete=models.CASCADE, blank=True, null=True, related_name='menusubitems')

    class Meta:
        verbose_name = 'Позиция'
        verbose_name_plural = 'Позиции'

    def __str__(self):
        return self.name
