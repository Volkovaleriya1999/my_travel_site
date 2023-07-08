from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.Destinations.as_view(), name='destinations'),
    path('tours_category/<slug:cat_slug>/', views.CategoryTour.as_view(), name='tours_cat' ),
    # path('countries/', views.ShowCountries.as_view(), name='countries'),
    path('detail_tour/<slug:tour_slug>/', views.detail_tour, name='tour'),
    path('comment/', views.CommentView.as_view(), name='comment'),
    # path('countries/<slug:country_slug>/', views.DetailCountry.as_view(), name='country'),
    # path('countries/<slug:country_slug>/<slug:tours_slug>/', views.show_tours_in_city, name='show_tours')

]


