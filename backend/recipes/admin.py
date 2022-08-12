from django.contrib import admin

from .models import (
    FavoriteRecipe, Ingredient, IngredientForRecipe, Recipe, ShoppingCart, Tag
)


@admin.register(Tag)
class TagsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'color',
        'slug',
    )


@admin.register(Ingredient)
class IngredientsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'measurement_unit',
    )
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(IngredientForRecipe)
class IngredientForRecipeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'ingredient',
        'recipe',
        'amount',
    )
    list_filter = ('recipe',)
    search_fields = ('recipe',)


class RecipeIngredientsInline(admin.TabularInline):
    model = IngredientForRecipe


@admin.register(Recipe)
class RecipesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'author',
        'name',
        'image',
        'text',
        'cooking_time',
        'favorite_count',
    )
    list_filter = ('author', 'name', 'tags')
    search_fields = ('name',)
    inlines = (RecipeIngredientsInline,)

    def favorite_count(self, recipe):
        return recipe.favorite.count()

    favorite_count.short_description = 'Количество добавлений в избранное'


@admin.register(FavoriteRecipe)
class FavoriteRecipeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'recipe',
    )


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'recipe',
    )
