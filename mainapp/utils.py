# from .models import News
# from django.db.models import Q
# from django.core.paginator import Paginator
#
#
# def paginate_projects(request, news, results):
#     page = request.GET.get('page', 1)
#     results = 1
#     paginator = Paginator(news, results, allow_empty_first_page=True)
#
#     news = paginator.get_page(page)
#
#     left_index = int(page) - 2
#     if left_index < 1:
#         left_index = 1
#
#     right_index = int(page) + 3
#     if right_index > paginator.num_pages:
#         right_index = paginator.num_pages + 1
#
#     custom_range = range(left_index, right_index)
#
#     return news, custom_range
#
#
# def search_news(request):
#     search_query = ''
#
#     if request.GET.get('search_query'):
#         search_query = request.GET.get('search_query')
#
#     new = News.objects.distinct().filter(Q(title__iregex=search_query) | Q(content__iregex=search_query))
#
#     return new, search_query