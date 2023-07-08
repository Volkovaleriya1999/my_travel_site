from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    MALE = 'M'
    FEMALE = "W"
    GENDER_CHOICES = (
        (MALE, 'M'),
        (FEMALE, 'W')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Пользователь')
    name = models.CharField(max_length=200, null=True, blank=True, verbose_name='Имя')
    email = models.EmailField(max_length=500, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True, verbose_name='Логин')
    bio = models.TextField(blank=True, verbose_name='О себе')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name='Пол')
    profile_image = models.ImageField(upload_to='profiles/', default='profiles/user-default.png', verbose_name='Фото')


    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f'{self.username}'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'