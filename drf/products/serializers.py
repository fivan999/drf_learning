import rest_framework.serializers

import products.models


class ProductSerializer(rest_framework.serializers.ModelSerializer):
    """сериализотор модели продукта"""

    class Meta:
        model = products.models.Product
        fields = (
            'name',
            'description',
            'created_at',
            'updated_at',
            'is_published',
            'category_id',
        )


# class ProductSerializer(rest_framework.serializers.Serializer):
#     """сериализатор продукта"""

#     name = rest_framework.serializers.CharField(max_length=150)
#     description = rest_framework.serializers.CharField()
#     created_at = rest_framework.serializers.DateTimeField(read_only=True)
#     updated_at = rest_framework.serializers.DateTimeField(read_only=True)
#     is_published = rest_framework.serializers.BooleanField(default=True)
#     category_id = rest_framework.serializers.IntegerField()
