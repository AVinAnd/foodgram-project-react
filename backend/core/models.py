from django.db import models
from django.core.validators import RegexValidator
from colorfield.fields import ColorField


class Tag(models.Model):
    """Модель тегов"""
    name = models.CharField(max_length=200)
    color = ColorField(default='#FFFFFF', null=True, max_length=7)
    slug = models.CharField(
        max_length=200,
        unique=True,
        null=True,
        validators=[RegexValidator(regex='^[-а-я-a-zA-Z0-9_]+$')]
    )

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """Модель ингредиентов"""
    name = models.CharField(max_length=200)
    measurement_unit = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'ингредиент'
        verbose_name_plural = 'ингредиенты'

    def __str__(self):
        return self.name
