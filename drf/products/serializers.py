import rest_framework.serializers

import products.models


class ProductSerializer(rest_framework.serializers.ModelSerializer):
    """сериализотор модели Product"""

    user = rest_framework.serializers.HiddenField(
        default=rest_framework.serializers.CurrentUserDefault()
    )

    class Meta:
        model = products.models.Product
        fields = (
            'name',
            'description',
            'is_published',
            'category',
            'user',
        )
        read_only_fields = ('created_at', 'updated_at')


class CategorySerializer(rest_framework.serializers.ModelSerializer):
    """сериализатор модели Category"""

    class Meta:
        model = products.models.Category
        fields = ('name',)
