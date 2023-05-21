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


class ProductAPIView(rest_framework.views.APIView):
    """список продуктов"""

    def get(
        self, request: django.http.HttpRequest
    ) -> django.http.HttpResponse:
        """получение списка продуктов"""
        product_list = products.models.Product.objects.all().values()
        return rest_framework.response.Response(
            {
                'get': products.serializers.ProductSerializer(
                    product_list, many=True
                ).data
            }
        )

    def post(
        self, request: django.http.HttpRequest
    ) -> django.http.HttpResponse:
        """создание продукта"""
        product_serializer = products.serializers.ProductSerializer(
            data=request.data
        )
        product_serializer.is_valid(raise_exception=True)
        product_serializer.save()
        return rest_framework.response.Response(
            {'post': product_serializer.data}
        )

    def put(
        self, request: django.http.HttpRequest, pk: int
    ) -> django.http.HttpResponse:
        """обновление продукта"""
        product = products.models.Product.objects.filter(pk=pk).first()
        if not product:
            return rest_framework.response.Response(
                {'error': 'product is not found'}
            )
        product_serializer = products.serializers.ProductSerializer(
            data=request.data, instance=product
        )
        product_serializer.is_valid(raise_exception=True)
        product_serializer.save()
        return rest_framework.response.Response(
            {'put': product_serializer.data}
        )

    def delete(
        self, request: django.http.HttpRequest, pk: int
    ) -> django.http.HttpResponse:
        """удаление продукта"""
        product = products.models.Product.objects.filter(pk=pk).first()
        if not product:
            return rest_framework.response.Response(
                {'error': 'product not found'}
            )
        product.delete()
        return rest_framework.response.Response({'delete': 'success'})
