import rest_framework.generics
import rest_framework.response
import rest_framework.views

import django.forms
import django.http

import products.models
import products.serializers


# class ProductsListAPIView(rest_framework.generics.ListAPIView):
#     """список продуктов"""

#     queryset = products.models.Product.objects.all()
#     serializer_class = products.serializers.ProductsSerializer


class ProductsListAPIView(rest_framework.views.APIView):
    """список продуктов"""

    def get(
        self, request: django.http.HttpRequest
    ) -> django.http.HttpResponse:
        """обработка get-запроса"""
        product_list = products.models.Product.objects.all().values()
        return rest_framework.response.Response(
            {
                'products': products.serializers.ProductSerializer(
                    product_list, many=True
                ).data
            }
        )

    def post(
        self, request: django.http.HttpRequest
    ) -> django.http.HttpResponse:
        """обработка post-запроса"""
        product_serializer = products.serializers.ProductSerializer(
            data=request.data
        )
        product_serializer.is_valid(raise_exception=True)

        new_product = products.models.Product.objects.create(
            name=request.data['name'],
            description=request.data['description'],
            category_id=request.data['category_id'],
        )
        return rest_framework.response.Response(
            {
                'success': products.serializers.ProductSerializer(
                    new_product
                ).data
            }
        )
