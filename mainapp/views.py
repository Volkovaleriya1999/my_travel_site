from django.shortcuts import render
from .models import News, Category
from django.views.generic import DetailView, ListView
from django.db.models import Count
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from tours.models import Tours
from .utils import *
from tours.models import Comment



def index(request):
    news = News.objects.all()[:3]
    tours = Tours.objects.all()[:3]
    comments = Comment.objects.all()[:3]
    context = {
        'news': news,
        'tours': tours,
        'comments': comments,
    }
    return render(request, 'mainapp/index.html', context)


def about(request):
    return render(request, 'mainapp/about.html')


def news(request):
    # news = News.objects.all()
    last_news = News.objects.all()[:2]
    categories = Category.objects.all()

    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    news = News.objects.distinct().filter(Q(title__iregex=search_query) | Q(content__iregex=search_query))

    page = request.GET.get('page', 1)
    results = 1
    paginator = Paginator(news, results)

    news = paginator.get_page(page)

    left_index = int(page) - 1
    if left_index < 1:
        left_index = 1

    right_index = int(page) + 2
    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)

    context = {
        'news': news,
        'search_query':search_query,
        'last_news': last_news,
        'categories': categories,
        'custom_range': custom_range,
    }
    # context.update(get_page_context(news, request))
    return render(request, 'mainapp/news.html', context)


def news_category(request, slug):
    # news = News.objects.filter(cat__slug=slug)
    categories = Category.objects.all()
    last_news = News.objects.all()[:2]


    news = News.objects.distinct().filter(cat__slug=slug)

    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    news = News.objects.distinct().filter(Q(title__iregex=search_query) | Q(content__iregex=search_query))

    page = request.GET.get('page', 1)
    results = 1
    paginator = Paginator(news, results, allow_empty_first_page=True)

    news = paginator.get_page(page)

    left_index = int(page) - 0
    if left_index < 1:
        left_index = 1

    right_index = int(page) + 1
    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(1, 3)

    context = {
        'categories': categories,
        'last_news': last_news,
        'news': news,
        'custom_range': custom_range,

    }
    # context.update(get_page_context(news, request))
    return render(request, 'mainapp/news.html', context)


# def get_page_context(queryset, request):
#     page = request.GET.get('page', 1)
#     results = 1
#     paginator = Paginator(queryset, results)
#
#     news = paginator.get_page(page)
#
#     left_index = int(page) - 1
#     if left_index < 1:
#         left_index = 1
#
#     right_index = int(page) + 2
#     if right_index > paginator.num_pages:
#         right_index = paginator.num_pages + 1
#
#     custom_range = range(left_index, right_index)
#
#     return {
#         'paginator': paginator,
#         'custom_range': custom_range,
#         'news': news,
#     }


class NewDetails(DetailView):
    """Детальное описание новости"""
    model = News
    slug_field = 'slug'
    context_object_name = 'new'




# class NewsList(ListView):
#     """Список новостей"""
#
#     model = News
#     template_name = 'mainapp/news.html'
#     context_object_name = 'news'
#
#     def get_queryset(self):
#         return News.objects.all().select_related('cat')
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # context['news'] = context['news']
#         context['cat_selected'] = 0
#         context['last_news'] = News.objects.all()[:2]
#         # context['categories'] = Category.objects.all()
#         return context




# class NewsCategory(ListView):
#     model = Category
#     template_name = 'mainapp/news.html'
#
#     context_object_name = 'category'
#     allow_empty = False
#
#     # def get_queryset(self):
#     #     return News.objects.filter(cat__slug=self.kwargs['cat_slug']).select_related('cat')
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # context['cat_selected'] = context['news'][0].cat.id
#         # context['cats'] = Category.objects.all()
#         # context['cats'] = Category.objects.annotate(Count('news'))
#         return context


# class Search(ListView):
#     """Поиск новостей"""
#     paginate_by = 1
#     template_name = 'mainapp/news.html'
#     context_object_name = 'news'
#
#     def get_queryset(self):
#         return News.objects.filter(Q(title__iregex=self.request.GET.get('q')) | Q(content__iregex=self.request.GET.get('q')))
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['q'] = f'q={self.request.GET.get("q")}'
#         return context


# def search(request):
#     if 'q' in request.GET:
#         q = request.GET.get('q')
#         products = News.objects.order_by('-created').filter(Q(title=q) | Q(content=q))
#         product_count = products.count()
#     context = {
#         'q': q,
#         'products': products,
#         'product_count': product_count,
#     }
#     return render(request, 'mainapp/news.html', context=context)



