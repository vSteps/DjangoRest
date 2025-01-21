"""
URL configuration for api_amazon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin # type: ignore
from django.urls import path, re_path, include # type: ignore
from rest_framework.routers import DefaultRouter # type: ignore
from app import views # type: ignore
from rest_framework import permissions # type: ignore
from drf_yasg.views import get_schema_view # type: ignore
from drf_yasg import openapi # type: ignore
from rest_framework import permissions # type: ignore
from app.views import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="API documentation with Swagger",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'Usuarios', views.UsuarioViewSet)
router.register(r'endereco', views.EnderecoViewSet)
router.register(r'pedidos', views.PedidoViewSet)
router.register(r'itens', views.ItemViewSet)
router.register(r'forma_pagamento', views.Forma_PagamentoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api_amazon/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),


    path('api/auth/registro/', RegistroUsuarioView.as_view(), name='registro'),
    path('api/auth/login/', LoginUsuarioView.as_view(), name='login'),
    path('api/auth/logout/', LogoutUsuarioView.as_view(), name='logout'),

    path('api/auth/registro/cliente/', ClienteRegistrationView.as_view(), name='registro-cliente'),
    path('api/auth/login/cliente/', ClienteLoginView.as_view(), name='login-cliente'),

    path('api/auth/registro/vendedor/', VendedorRegistrationView.as_view(), name='registro-vendedor'),
    path('api/auth/login/vendedor/', VendedorLoginView.as_view(), name='login-vendedor'),
]

