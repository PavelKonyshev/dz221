from django.conf import settings
from django.urls import path
from django.views.decorators.cache import cache_page

from .apps import CatalogConfig
from .views import ProductListView, ProductDetailView, ContactPageView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, toggle_in_stock, CategoryListView
from django.conf.urls.static import static
app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("contacts/", ContactPageView.as_view(), name="contacts"),
    path("products/<int:pk>/", cache_page(60)(ProductDetailView.as_view()), name="product_detail"),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('activity/<int:pk>/delete/', toggle_in_stock, name='toggle_in_stock'),
    path('categories/', CategoryListView.as_view(), name='categories_list')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


