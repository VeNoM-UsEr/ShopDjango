from django.db import models
from djmoney.models.fields import MoneyField

class Category(models.Model):
    title = models.CharField(
        "Название"
    )
    position = models.PositiveIntegerField(
        verbose_name="Позиция"
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"
        
class Product(models.Model):
    title = models.CharField(
        "Название"
    )
    description = models.TextField(
        "Описание",
        null=True,
        blank=True
    )
    photo = models.ImageField(
        verbose_name="Фотография",
        null=True,
        blank=True,
        upload_to='products/'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория"
    )
    price = MoneyField(
        verbose_name="Цена",
        max_digits=12,
        decimal_places=2,
        
    )
    def __str__(self):
        return self.title
    
    
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"