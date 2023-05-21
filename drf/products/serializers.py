import rest_framework.serializers

import products.models


# class ProductSerializer(rest_framework.serializers.ModelSerializer):
#     """сериализотор модели продукта"""

#     class Meta:
#         model = products.models.Product
#         fields = (
#             'name',
#             'description',
#             'created_at',
#             'updated_at',
#             'is_published',
#             'category_id',
#         )


class ProductSerializer(rest_framework.serializers.Serializer):
    """сериализатор продукта"""

    name = rest_framework.serializers.CharField(max_length=150)
    description = rest_framework.serializers.CharField()
    created_at = rest_framework.serializers.DateTimeField(read_only=True)
    updated_at = rest_framework.serializers.DateTimeField(read_only=True)
    is_published = rest_framework.serializers.BooleanField(default=True)
    category_id = rest_framework.serializers.IntegerField()

    def create(self, validated_data: dict) -> products.models.Product:
        """создание записи продукта в бд"""
        return products.models.Product.objects.create(**validated_data)

    def update(
        self, instance: products.models.Product, validated_data: dict
    ) -> products.models.Product:
        """обновление записи о продукте"""
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get(
            'description', instance.description
        )
        instance.category_id = validated_data.get(
            'category_id', instance.category_id
        )
        instance.is_published = validated_data.get(
            'is_published', instance.is_published
        )
        instance.save()
        return instance
