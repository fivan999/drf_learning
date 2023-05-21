import django.urls

import products.views


app_name = 'products'

urlpatterns = [
    django.urls.path(
        'products/', products.views.ProductsListAPIView.as_view(), name='list'
    )
]
