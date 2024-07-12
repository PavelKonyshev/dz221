
from config.settings import CACHE_ENABLED
from catalog.models import Product, Category
from django.core.cache import cache


def get_product_from_cache():
    """Получаем продукты из кэша, если кэш пустполучаем данные из БД"""
    if not CACHE_ENABLED:
        return Product.objects.all()
    else:
        key = "prodocts_list"
        product = cache.get(key)
        if product is not None:
            return product
        else:
            product = Product.objects.all()
            cache.set(key, product)
            return product

def get_categories_from_cache():
    if not CACHE_ENABLED:
        return Category.objects.all()
    else:
        key = 'categories_list'
        categories = cache.get(key)
        if categories is not None:
            return categories
        else:
            categories = Category.objects.all()
            cache.set(key, categories)
            return categories