from django.db import models
from django.urls import reverse


# Create your models here.



class Tours(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='URL')
    description = models.CharField(max_length=1000, verbose_name='Описание')
    start_date = models.DateField(null=True, blank=True, verbose_name='Дата начала')
    end_date = models.DateField(null=True, blank=True, verbose_name='Дата конца')
    tour_type = models.ForeignKey('TourType', on_delete=models.PROTECT, verbose_name='Тип тура')
    food_type = models.ForeignKey('FoodType', on_delete=models.PROTECT, verbose_name='Тип питания')
    hotel = models.ForeignKey('Hotels', on_delete=models.PROTECT, verbose_name='Отель', related_name='tours_hotel')
    departure = models.ForeignKey('Flights', on_delete=models.PROTECT, related_name='dep', verbose_name='Вылет')
    arrival = models.ForeignKey('Flights', on_delete=models.PROTECT, related_name='arri', verbose_name='Прилет')
    price = models.CharField(max_length=20, null=True, blank=True, verbose_name='Цена')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'
        ordering = ('id',)

    def get_absolute_url(self):
        return reverse('tour', kwargs={'slug': self.slug})



class Hotels(models.Model):
    STARS_CHOICES = (
        ('1', '*'),
        ('2', '* *'),
        ('3', '* * *'),
        ('4', '* * * *'),
        ('5', '* * * * *'),

    )
    name = models.CharField(max_length=255, null=True, blank=True)
    stars = models.CharField(max_length=10, choices=STARS_CHOICES, verbose_name='Звезды')
    city = models.ForeignKey('Cities', on_delete=models.PROTECT, verbose_name='Город', related_name='hotel_city')
    description = models.TextField(verbose_name='Описание')
    type_allocation = models.ForeignKey('TypeAllocation', on_delete=models.PROTECT, verbose_name='Тип размещения')
    image = models.ImageField(upload_to='tours/', null=True, blank=True, verbose_name='Фото')
    image1 = models.ImageField(upload_to='tours/', null=True, blank=True, verbose_name='Фото')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отель'
        verbose_name_plural = 'Отели'
        ordering = ('id',)



class TourType(models.Model):
    tour_type = models.CharField(max_length=255, null=True, blank=True, verbose_name='Тип тура')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='URL')

    def __str__(self):
        return self.tour_type

    class Meta:
        verbose_name = 'Тип тура'
        verbose_name_plural = 'Типы туров'
        ordering = ('id',)


    def get_absolute_url(self):
        return reverse('tour_type', kwargs={'slug': self.slug})


class TypeAllocation(models.Model):
    type_allocation = models.CharField(max_length=255, null=True, blank=True, verbose_name='Тип размещения')

    def __str__(self):
        return self.type_allocation

    class Meta:
        verbose_name = 'Тип размещения'
        verbose_name_plural = 'Типы размещения'
        ordering = ('id',)



class FoodType(models.Model):
    food_type = models.CharField(max_length=255, null=True, blank=True, verbose_name='Тип питания')

    def __str__(self):
        return self.food_type

    class Meta:
        verbose_name = 'Тип питания'
        verbose_name_plural = 'Типы питания'
        ordering = ('id',)



class Flights(models.Model):
    flight_number = models.CharField(max_length=255, null=True, blank=True, verbose_name='Номер рейса')
    city_departure = models.CharField(max_length=255, null=True, blank=True, verbose_name='Город вылета')
    date_departure = models.DateField(null=True, blank=True, verbose_name='Дата вылета')
    time_departure = models.CharField(max_length=20, null=True, blank=True, verbose_name='Время вылета')
    city_arrival = models.CharField(max_length=255, null=True, blank=True, verbose_name='Город прилета')
    date_arrival = models.DateField(null=True, blank=True, verbose_name='Дата прилета')
    time_arrival = models.CharField(max_length=20, null=True, blank=True, verbose_name='Время Прилета')


    def __str__(self):
        return self.flight_number

    class Meta:
        verbose_name = 'Рейс'
        verbose_name_plural = 'Рейсы'
        ordering = ('id',)



class Cities(models.Model):
    city = models.CharField(max_length=255, null=True, blank=True, verbose_name='Город')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='URL')
    country = models.ForeignKey('Countries',  on_delete=models.PROTECT, related_name='country_in_city',
                                verbose_name='Страна')
    image = models.ImageField(upload_to='tours/', verbose_name='Фото')

    def __str__(self):
        return self.city

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ('id',)


    def get_absolute_url(self):
        return reverse('city', kwargs={'slug': self.slug})


class Countries(models.Model):
    country = models.CharField(max_length=255, null=True, blank=True, verbose_name='Страна')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='URL')
    image = models.ImageField(upload_to='tours/', verbose_name='Фото')

    def __str__(self):
        return self.country

    class Meta:
        verbose_name = 'Страну'
        verbose_name_plural = 'Страны'
        ordering = ('id',)


    def get_absolute_url(self):
        return reverse('country', kwargs={'slug': self.slug})


class Comment(models.Model):
    tour = models.ForeignKey(Tours, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80, verbose_name='Имя')
    email = models.EmailField()
    body = models.TextField(verbose_name='Текст')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'{self.name}, {self.tour}'
