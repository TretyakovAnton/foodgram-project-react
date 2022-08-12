from django.db import models
from django.db.models import UniqueConstraint

from users.models import User


class Tag(models.Model):
    """
    Модель тегов.
    """
    name = models.CharField(
        max_length=200,
        verbose_name='Наименование тэга',
        help_text='Введите наименование тэга'
    )

    color = models.CharField(
        max_length=7,
        verbose_name='HEX-код цвета',
    )

    slug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name='Slug',
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """
    Модель ингредиентов.
    """
    name = models.CharField(
        max_length=200,
        verbose_name='Наименование ингредиента',
        help_text='Введите название ингредиента'
    )

    measurement_unit = models.CharField(
        max_length=15,
        verbose_name='Еденица измерения',
        help_text='Введите еденицу измерения'
    )

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        constraints = [
            UniqueConstraint(
                fields=['name', 'measurement_unit'],
                name='unique_ingredient'
            )
        ]

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """
    Модель рецептов.
    """
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор рецепта',
        help_text='Автор рецепта'
    )

    ingredients = models.ManyToManyField(
        Ingredient,
        verbose_name='Ингредиенты',
        through='IngredientForRecipe',
        related_name='recipes_ingredients',
        help_text='Выберите ингредиенты',
    )

    tags = models.ManyToManyField(
        Tag,
        verbose_name='Тэги',
        help_text='Выберите тэги',
        related_name='recipes_tag',
    )

    image = models.ImageField(
        upload_to='recipes/',
        verbose_name='Фото блюда',
        help_text='Фото отображаемая в рецепте с блюдом'
    )

    name = models.CharField(
        max_length=200,
        verbose_name='Название рецепта',
        help_text='Введите название рецепта'
    )

    text = models.TextField(
        verbose_name='Описание рецепта',
        help_text='Введите описание рецепта'
    )

    cooking_time = models.PositiveIntegerField(
        verbose_name='Время готовки в минутах',
        help_text='Введите время готовки в минутах',
    )

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ('-id',)

    def __str__(self):
        return self.name


class IngredientForRecipe(models.Model):
    """
    Модель в которой находится количество ингредиентов для рецепта.
    """
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепт',
        related_name='ingredient_for_recipe',
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        verbose_name='Ингредиент',
        related_name='ingredient_for_recipe',
    )
    amount = models.PositiveSmallIntegerField(
        verbose_name='Количество',
        help_text='Введите количество ингредиента для рецпта'
    )

    class Meta:
        verbose_name = 'Ингредиент в рецепте'
        verbose_name_plural = 'Ингредиенты в рецепте'
        constraints = [
            UniqueConstraint(
                fields=['recipe', 'ingredient'],
                name='unique_ingredient_for_recipe'
            )
        ]

    def __str__(self):
        return f'Количество{self.ingredient} в {self.recipe}:{self.amount}'


class FavoriteRecipe(models.Model):
    """
    Модель избранных рецептов.
    """
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепт',
        related_name='favorite',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='favorite',
    )

    class Meta:
        verbose_name = 'Любимый рецепт'
        verbose_name_plural = 'Любимые рецепты'
        constraints = (
            UniqueConstraint(
                fields=('recipe', 'user'),
                name='unique_favorite',
            ),
        )

    def __str__(self):
        return f'Рецепт {self.recipe} в избранном пользователя {self.user}'


class ShoppingCart(models.Model):
    """
    Модель корзины покупок.
    """
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепт',
        related_name='shopping_cart'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='shopping_cart',
    )

    class Meta:
        verbose_name = 'Список покупок'
        verbose_name_plural = 'Списки покупок'
        constraints = (
            UniqueConstraint(
                fields=('recipe', 'user'),
                name='unique_shopping_cart',
            ),
        )

    def __str__(self):
        return f'{self.recipe} в корзине у пользователя {self.user}'
