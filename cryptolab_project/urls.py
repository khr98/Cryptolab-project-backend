from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings


schema_url_patterns = [
    path('', include('user.urls')),
]

schema_view_v1 = get_schema_view(
    openapi.Info(
        title="Cryptolab-project-backend",
        default_version='v1',
        description="Cryptolab-project-backend API 명세서",
        terms_of_service="https://www.google.com/policies/terms/",
    ),
    public=True,
    permission_classes=(AllowAny,),
    patterns=schema_url_patterns,
)


urlpatterns = [
    # path('api_auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('user.urls')),
    path('admin/', admin.site.urls),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view_v1.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view_v1.with_ui('swagger',
                                                  cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view_v1.with_ui('redoc',
                                                cache_timeout=0), name='schema-redoc'),
]