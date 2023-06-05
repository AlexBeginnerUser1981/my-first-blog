from django.urls import include, path
from rest_framework import routers
from . import views, viewshtml
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework_extensions.routers import ExtendedDefaultRouter

#router = ExtendedDefaultRouter()
router = routers.DefaultRouter()
router.register(r'potions', views.PotionViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'subcategory', views.SubCategoryViewSet)
router.register(r'type', views.TypeViewSet)
router.register(r'color', views.ColorViewSet)
router.register(r'body', views.BodyViewSet)
router.register(r'productionmethod', views.ProductionMethodViewSet)
router.register(r'brand', views.BrandViewSet)
router.register(r'manufacturer', views.ManufacturerViewSet)
router.register(r'region', views.RegionViewSet, basename='region')
router.register(r'country', views.CountryViewSet, basename='country')
router.register(r'rawmaterial', views.RawMaterialViewSet)
router.register(r'variety', views.VarietyViewSet)
router.register(r'food', views.FoodViewSet)
router.register(r'users', views.UserViewSet) #, basename='user')
router.register(r'groups', views.GroupViewSet),
router.register(r'labels', views.ReadingLabelViewSet)
urlpatterns = [
	path('', include(router.urls)),
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	path('openapi', get_schema_view(
        title="Your Project",
        description="API for all things …",
        version="1.0.0"
    ), name='openapi-schema'),
	path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
	path('redoc/', TemplateView.as_view(
        template_name='redoc.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='redoc'),
	path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
        path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
	
	path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

]