from django.shortcuts import render, redirect
from .models import *
from django.views.generic import DetailView, ListView, CreateView
from .forms import CommentForm
from django.urls import reverse_lazy
from cart.forms import CartAddProductForm
from django.shortcuts import get_object_or_404
from django.db.models import Q



class Destinations(ListView):
    """Список Туров"""
    paginate_by = 3
    model = Tours
    template_name = 'tours/destinations.html'
    context_object_name = 'tours'

    def get_queryset(self):
        queryset = super(Destinations, self).get_queryset()
        sort = self.request.GET.get('sort')

        search_arrival_city = self.request.GET.get("search_arrival_city")
        search_dep_city = self.request.GET.get("search_dep_city")
        search_date = self.request.GET.get("search_date")
        search_budget = self.request.GET.get("search_budget")
        # search_query = search_query1 | search_query2 | search_query3 | search_query4
        # print(search_query)
        print(search_date)
        print(search_budget)
        print(search_arrival_city)
        print(search_dep_city)

        if search_arrival_city and search_dep_city and search_date and search_budget:
            arri = queryset.filter(departure__city_arrival__iregex=search_arrival_city)
            dep = queryset.filter(departure__city_departure__iregex=search_dep_city)
            date = queryset.filter(start_date=search_date)
            price = queryset.filter(price__lte = search_budget)
            print(arri, dep, date, price)

            q = queryset.filter(Q(departure__city_departure__iregex=search_dep_city) & Q(departure__city_arrival__iregex=search_arrival_city) & Q(start_date=search_date) & Q(price__lte=search_budget))
            print(q)

            if q:
                return q

            else:
                print('таких туров нет')

        if sort == ('цена возрастание'):
            return queryset.order_by('price')
        if sort == ('цена убывание'):
            return queryset.order_by('-price')
        if sort == ('название'):
            return queryset.order_by('name')
        else:
            return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = TourType.objects.all()
        # context['sort_price'] = Tours.objects.all().sort_by('price')
        # context['tours'] = Tours.objects.all()
        return context


class CategoryTour(ListView):
    model = Tours
    paginate_by = 3
    context_object_name = 'tours'
    template_name = 'tours/destinations.html'

    # def get_queryset(self):
    #     return Tours.objects.filter(tour_type__slug=self.kwargs['slug'])

    def get_queryset(self):
        queryset = super(CategoryTour, self).get_queryset().filter(tour_type__slug=self.kwargs['cat_slug'])
        sort = self.request.GET.get('sort')
        if sort == ('цена возрастание'):
            return queryset.order_by('price')
        if sort == ('цена убывание'):
            return queryset.order_by('-price')
        if sort == ('название'):
            return queryset.order_by('name')
        else:
            return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = TourType.objects.all()

        return context



# def category_tour(request, slug):
#
#     tours = Tours.objects.filter(tour_type__slug=slug)
#     category = TourType.objects.all()
#
#
#     page = request.GET.get('page', 1)
#     results = 3
#     paginator = Paginator(tours, results)
#
#     tours = paginator.get_page(page)
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
#     context = {
#         'tours': tours,
#         'category': category,
#         'custom_range': custom_range,
#     }
#     # context.update(get_page_context(news, request))
#     return render(request, 'tours/destinations.html', context)


# class DetailTour(DetailView):
#     model = Tours
#     slug_field = 'slug'
#     context_object_name = 'tour'
#     template_name = 'tours/tour_detail.html'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['cart_product_form'] = CartAddProductForm()
#
#
#         return context


def detail_tour(request, tour_slug):
    tour = get_object_or_404(Tours, slug=tour_slug)

    comments = tour.comments.filter(active=True)

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.tour = tour
            new_comment.save()
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        comment_form = CommentForm()

    context = {
        'tour': tour,
        'cart_product_form': CartAddProductForm(),
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'tours/tour_detail.html', context)


class CommentView(CreateView):
    model = Comment
    form_class = CommentForm
    success_url = reverse_lazy('tour')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        form = CommentForm(initial={'tour': kwargs['pk']})
        context = {'form': form}
        return render(request, 'add_comment.html', context)


# class ShowCountries(ListView):
#     paginate_by = 3
#     model = Countries
#     template_name = 'tours/countries.html'
#     context_object_name = 'countries'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         return context


# class DetailCountry(ListView):
#     model = Countries
#     context_object_name = 'country'
#     template_name = 'tours/country_detail.html'
#
#     def get_queryset(self, *args, **kwargs):
#         return Countries.objects.filter(slug=self.kwargs['country_slug'])
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['countries'] = Countries.objects.all()
#
#
#         return context


# def show_tours_in_city(request, country_slug, tours_slug):
#     cities = Countries.objects.filter(slug=country_slug)
#     tours_in_city = Tours.objects.filter(slug=tours_slug)
#     context = {
#         'cities': cities,
#         'tours_in_city': tours_in_city,
#     }
#     return render(request, 'tours/tours-in-city.html', context)

