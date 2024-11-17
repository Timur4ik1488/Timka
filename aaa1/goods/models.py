from django.db import models

#создали миграции, данные для типов данных, которые заносятся в БД ищи в документации django

class Categories(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name= 'Название')
    slug = models.SlugField(max_length= 200, unique = True, blank= True, null=True, verbose_name= 'URL')


    class Meta:
        db_table = 'category' #принято создавать таблицы для БД в единственном числе
        # здесь идёт изменение языка именно для слов в самой админ-панели
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name #данная конструкция переприсваивает имя для названия категорий в админ-панели( теперь категория там называется ВСЕ ТОВАРЫ, а не херня с индексом)




class Products(models.Model): # лучше всего до этого прочитать документацию на сайте джанго для создания таблиц 
    name = models.CharField(max_length=100, unique=True, verbose_name= 'Название')#Добавляем название товара
    slug = models.SlugField(max_length= 200, unique = True, blank= True, null=True, verbose_name= 'URL')#Добавляем айди или код товара
    descriptions = models.TextField(blank=True, null=True, verbose_name='Описание')#Добавляем описание товара
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, height_field=None, width_field=None, max_length=None, verbose_name= 'Изображение')#Прикрепляем изображение нового товара
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=3, verbose_name= 'Цена')#Вводим цену товара уже с ограничениями на длину символов до и полсе запятой
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=3, verbose_name= 'Скидка в процентах')#Можно добавить скидку
    quantily = models.IntegerField(default=0, verbose_name= 'Количество')#Вводим количество товаров
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='категория') #связываем несколько таблиц друг с другом


    class Meta:
        db_table = 'product'
        verbose_name = 'продукт'
        verbose_name_plural = 'Продукты'

        def __str__(self):
            return f'{self.name} Количество - {self.quantity}' #идентичный случай, смотри выше в class Meta
     