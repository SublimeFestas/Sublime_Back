from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView)
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenRefreshView

from uploader.router import router as uploader_router

from core.views import UserViewSet, SalaoViewSet, EnderecoViewSet, AluguelViewSet, DecoracaoViewSet, TokenViewSet, ServicoViewset


router = DefaultRouter()

router.register(r'usuarios', UserViewSet, basename='usuarios')
router.register(r'salões', SalaoViewSet, basename='salões')
router.register(r'endereços', EnderecoViewSet, basename='endereços')
router.register(r'alugueis', AluguelViewSet, basename='alugueis')
router.register(r'decoracoes', DecoracaoViewSet, basename='decoracoes')
router.register(r'servicos', ServicoViewset, basename='serviços')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/media/", include(uploader_router.urls)),
    # OpenAPI 3
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/swagger/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
    path(
        'api/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc',
    ),
    # API
    path('api/', include(router.urls)),
    path('api/token/', TokenViewSet.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenViewSet.as_view(), name='token_refresh'),
    
]
urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
