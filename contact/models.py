from django.db import models


class Contact(models.Model):
    """Подписка на email"""
    name = models.CharField(max_length=150, verbose_name='Имя')
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.email
