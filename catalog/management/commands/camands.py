import json
from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Seeds the database with initial data"

    def handle(self, *args, **kwargs):
        # Удаляем старые данные
        Category.objects.all().delete()
        Product.objects.all().delete()

        # Загружаем данные из JSON-файла
        with open("catalog/fixtures.catalog_data.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        # Создаем категории и продукты
        for item in data:
            model = item["model"]
            fields = item["fields"]

            if model == "catalog.category":
                Category.objects.create(id=item["pk"], **fields)
            elif model == "catalog.product":
                Product.objects.create(id=item["pk"], **fields)

        self.stdout.write(self.style.SUCCESS("Database has been seeded."))
