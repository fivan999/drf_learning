# Generated by Django 4.2 on 2023-05-23 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('products', '0002_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(
                help_text='Категория, к которой относится продукт',
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name='products',
                to='products.category',
                verbose_name='категория',
            ),
        ),
    ]