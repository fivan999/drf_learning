import rest_framework.permissions
import rest_framework.views

import django.http

import products.models


class IsProductOwnerOrAdminOrReadOnly(
    rest_framework.permissions.BasePermission
):
    """юзер или создатель продукта, или админ, или только смотрит"""

    def has_object_permission(
        self,
        request: django.http.HttpRequest,
        view: rest_framework.views.APIView,
        obj: products.models.Product,
    ):
        return (
            request.method in rest_framework.permissions.SAFE_METHODS
            or obj.user == request.user
            or request.user.is_staff
        )
