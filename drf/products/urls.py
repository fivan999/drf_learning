import django.urls

import products.views


app_name = 'products'

urlpatterns = [
    django.urls.path(
        'products/', products.views.ProductAPIView.as_view(), name='list'
    ),
    django.urls.path(
        'products/<int:pk>/',
        products.views.ProductAPIView.as_view(),
        name='detail',
    ),
]
