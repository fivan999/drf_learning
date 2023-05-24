import django.urls

import products.views


# router = rest_framework.routers.SimpleRouter()
# router.register(
#     r'products', products.views.ProductViewSet, basename='product'
# )

app_name = 'products'

urlpatterns = [
    # django.urls.path('', django.urls.include(router.urls)),
    django.urls.path(
        'products/',
        products.views.ProductListCreateAPIView.as_view(),
        name='list-create',
    ),
    django.urls.path(
        'products/<int:pk>/',
        products.views.ProductRetreiveUpdateDestroyAPIView.as_view(),
        name='list-create',
    ),
]
