from django.contrib import admin
from django.urls import include, path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


shema_view = get_schema_view(
    openapi.Info(
        title='Referral system API',
        default_version='v1',
        description='API for test referral system',
    ),
    public=True
)
urlpatterns = [
    path('api/', include('users.urls')),
    path('swagger/', shema_view.with_ui(
        'swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', shema_view.with_ui(
        'redoc', cache_timeout=0), name='schema-redoc')
]