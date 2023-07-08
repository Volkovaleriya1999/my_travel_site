from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='URL')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})


class News(models.Model):
    title = models.CharField(max_length=220, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='URL')
    content = models.TextField(null=True, blank=True, verbose_name='Содержание')
    photo = models.ImageField(upload_to='mainapp/%Y/%m/%d/', default='default.jpg', verbose_name='Фото')
    cat = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created']

    def get_absolute_url(self):
        return reverse('new', kwargs={'new_slug': self.slug})

    # def get_vote_count(self):
    #     count_news = self.category_set.all()
    #     up_votes = count_news.filter(value='up').count()
    #     total_votes = count_news.count()
    #
    #     ratio = (up_votes / total_votes) * 100
    #     self.vote_total = total_votes
    #     self.vote_ratio = ratio
    #
    #     self.save()


