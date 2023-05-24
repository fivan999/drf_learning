import rest_framework.decorators
import rest_framework.generics
import rest_framework.permissions
import rest_framework.response
import rest_framework.viewsets

import products.models
import products.permissions
import products.serializers


# class ProductViewSet(rest_framework.viewsets.ModelViewSet):
#     """вюсет для продукта"""

#     serializer_class = products.serializers.ProductSerializer

#     def get_queryset(self) -> django.db.models.QuerySet:
#         data = products.models.Product.objects.select_related('category')
#         pk = self.kwargs.get('pk')
#         if pk:
#             return data.filter(pk=pk)
#         return data[:3]

#     @rest_framework.decorators.action(methods=['get'], detail=True)
#     def category(
#         self, request: django.http.HttpRequest, pk: int
#     ) -> django.http.HttpResponse:
#         """получаем категорию нужного прдукта"""
#         category = products.models.Category.objects.filter(
#             products__pk=pk
#         ).first()
#         response_data = (
#             {'category': category.name}
#             if category
#             else {'detail': 'Страница не найдена.'}
#         )
#         return rest_framework.response.Response(response_data)

#     @rest_framework.decorators.action(methods=['get'], detail=False)
#     def categories(
#         self, request: django.http.HttpRequest
#     ) -> django.http.HttpResponse:
#         """список категорий"""
#         return rest_framework.response.Response(
#             {
#                 'categories':
#                 products.serializers.CategorySerializer(
#                     products.models.Category.objects.all(), many=True
#                 ).data
#             }
#         )


class ProductListCreateAPIView(rest_framework.generics.ListCreateAPIView):
    """список продуктов и их создание"""

    serializer_class = products.serializers.ProductSerializer
    permission_classes = (
        rest_framework.permissions.IsAuthenticatedOrReadOnly,
    )

    def get_queryset(self):
        return products.models.Product.objects.all()[:3]


class ProductRetreiveUpdateDestroyAPIView(
    rest_framework.generics.RetrieveUpdateDestroyAPIView
):
    """обновление и удаление отдельного продукта"""

    queryset = products.models.Product
    serializer_class = products.serializers.ProductSerializer
    permission_classes = (
        products.permissions.IsProductOwnerOrAdminOrReadOnly,
    )
