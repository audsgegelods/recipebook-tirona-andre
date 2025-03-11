from django.db import models
from django.urls import reverse


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ledger:recipe-detail', args=[self.pk])


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ledger:recipe-detail', args=[self.pk])


class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=50)
    ingredient = models.ForeignKey(Ingredient,
                                   related_name='recipe',
                                   on_delete=models.SET_NULL,
                                   null=True,)
    recipe = models.ForeignKey(Recipe,
                               related_name='ingredients',
                               on_delete=models.SET_NULL,
                               null=True,)
