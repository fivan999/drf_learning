# Generated by Django 4.2 on 2023-05-23 17:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('products', '0006_alter_product_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(
                auto_now=True,
                help_text='Время обновления продукта',
                verbose_name='время обновления',
            ),
        ),
    ]