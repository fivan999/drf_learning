import django.db.models


class Category(django.db.models.Model):
    """модель категории"""

    name = django.db.models.CharField(
        verbose_name='название', help_text='Название категории', max_length=150
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self) -> str:
        """строковое представление категории"""
        return self.name


class Product(django.db.models.Model):
    """модель продукта"""

    name = django.db.models.CharField(
        verbose_name='имя', help_text='Имя продукта', max_length=150
    )

    description = django.db.models.TextField(
        verbose_name='описание', help_text='Описание продукта'
    )

    created_at = django.db.models.DateTimeField(
        auto_now_add=True,
        verbose_name='время создания',
        help_text='Время создания продукта',
    )

    updated_at = django.db.models.DateTimeField(
        auto_now=True,
        verbose_name='время обновления',
        help_text='Время обновления продукта',
    )

    is_published = django.db.models.BooleanField(
        verbose_name='опубликован',
        help_text='Опубликован продукт или нет',
        default=True,
    )

    category = django.db.models.ForeignKey(
        verbose_name='категория',
        help_text='Категория, к которой относится продукт',
        to=Category,
        on_delete=django.db.models.DO_NOTHING,
    )

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

    def __str__(self) -> str:
        """строковое представление продукта"""
        return self.name
