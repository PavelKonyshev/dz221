from django.db import models

NULLABLE = {"blank": True, "null": True}


# Создание класса Категория
class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название категории", **NULLABLE
    )
    description = models.TextField(verbose_name="Описание категории", **NULLABLE)



    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name",]

    def __str__(self):
        return self.name
# Создание класса продукт
class Product(models.Model):

    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Введите наименование продукта", **NULLABLE
    )
    description = models.TextField(verbose_name="Описание", **NULLABLE)
    image = models.ImageField(
        upload_to="products/", verbose_name="Фото продукта", **NULLABLE
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        related_name="products", **NULLABLE
    )
    price = models.IntegerField(verbose_name="Цена продукта", **NULLABLE)
    created_at = models.DateField(verbose_name="Дата создания", **NULLABLE)
    updated_at = models.DateField(verbose_name="Дата изменения", **NULLABLE)
    in_stock = models.BooleanField(default=True)
    number_views = models.PositiveIntegerField(
        verbose_name="Количество просмотров",
        help_text="Укажите количество просмотров",
        default=0,
    )

    def __str__(self):
        return f"{self.name} {self.price}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "price", "created_at", "updated_at"]
        permissions = [
            ('can_change_in_stock', 'Can change in stock'),
            ('can_edit_description', 'Can edit description'),
            ('can_edit_category', 'Can edit category')
        ]





class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт', related_name='prod')
    version_number = models.IntegerField(verbose_name="номер версии")
    name = models.CharField(verbose_name="название версии")
    is_active = models.BooleanField(verbose_name="активная версия")

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'

    def __str__(self):
        return self.name