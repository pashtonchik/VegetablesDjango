from django.db import models


class Vegetable(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    price = models.IntegerField(verbose_name='Цена')
    image1 = models.ImageField(upload_to='images', blank=False, verbose_name='Фото')
    WEIGHTS = (
        ("G", "грамм"),
        ("KG", "килограмм"),
    )
    weight = models.CharField(max_length=2, choices=WEIGHTS, verbose_name='Еденица измерения массы')

    def __str__(self):
        return self.title


class Customer(models.Model):
    name = models.CharField(max_length=100, verbose_name='ФИО клиента')
    telegram_id = models.CharField(max_length=15, verbose_name='Telegram id')
    phone_number = models.CharField(max_length=11, verbose_name='Номер телефона')

    def __str__(self):
        return self.name


class OrderList(models.Model):
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    customer = models.ForeignKey(to=Customer, on_delete=models.PROTECT, verbose_name='ФИО клиента')
    shipping_address = models.CharField(max_length=128, verbose_name='Адрес доставки')
    is_paid = models.BooleanField(default=False, verbose_name='Оплата совершена')
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    edit_date = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return f'Заказ №{self.id}'


class OrderItem(models.Model):
    class Meta:
        verbose_name = 'Список товаров'
        verbose_name_plural = 'Список товаров'

    order_id = models.ForeignKey(to=OrderList, on_delete=models.PROTECT, related_name='order_items')
    vegetable_id = models.ForeignKey(to=Vegetable, on_delete=models.DO_NOTHING, verbose_name='Товар')
    quantity = models.IntegerField(verbose_name='Количество')
