from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Opply API')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("shop.urls")),

    path("openapi/", get_schema_view(), name="openapi-schema"),
    path(
        "docs/",
        TemplateView.as_view(
            template_name="swagger.html", extra_context={"schema_url": "openapi-schema"}
        ),
    ),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
