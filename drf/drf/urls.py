import rest_framework_simplejwt.views

import django.conf
import django.conf.urls.static
import django.contrib.admin
import django.contrib.staticfiles.urls
import django.urls


urlpatterns = [
    django.urls.path('admin/', django.contrib.admin.site.urls),
    django.urls.path('api/', django.urls.include('products.urls')),
    django.urls.path('api/auth/', django.urls.include('rest_framework.urls')),
    # django.urls.path('api/auth/', django.urls.include('djoser.urls')),
    # django.urls.re_path(
    #     r'^auth/', django.urls.include('djoser.urls.authtoken')
    # ),
    django.urls.path(
        'api/token/',
        rest_framework_simplejwt.views.TokenObtainPairView.as_view(),
        name='token_obtain_pair',
    ),
    django.urls.path(
        'api/token/refresh/',
        rest_framework_simplejwt.views.TokenRefreshView.as_view(),
        name='token_refresh',
    ),
    django.urls.path(
        'api/token/verify/',
        rest_framework_simplejwt.views.TokenVerifyView.as_view(),
        name='token_verify',
    ),
]

if django.conf.settings.DEBUG:
    urlpatterns += (
        django.urls.path(
            '__debug__/', django.urls.include('debug_toolbar.urls')
        ),
    )
    if django.conf.settings.MEDIA_ROOT:
        urlpatterns += django.conf.urls.static.static(
            django.conf.settings.MEDIA_URL,
            document_root=django.conf.settings.MEDIA_ROOT,
        )
    else:
        urlpatterns += (
            django.contrib.staticfiles.urls.staticfiles_urlpatterns()
        )
