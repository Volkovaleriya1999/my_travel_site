from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe





@admin.register(Tours)
class ToursAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
    list_display = ('id', 'name', 'tour_type', 'hotel', 'price')
    list_display_links = ('id', 'name', 'tour_type', 'hotel')
    list_filter = ('start_date', 'tour_type', 'food_type', 'hotel')
    save_on_top = True


@admin.register(Hotels)
class HotelsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'stars', 'city', 'get_image')
    list_display_links = ('id', 'name', 'stars', 'city', 'get_image')
    list_filter = ('name', 'stars', 'city')
    save_on_top = True

    def get_image(self, object):
        if object.image:
            return mark_safe(f'<img src="{object.image.url}" width="50">')

    get_image.short_description = 'Миниатюра'


@admin.register(TourType)
class TourTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'tour_type', 'slug')
    list_display_links = ('id', 'tour_type', 'slug')
    save_on_top = True


@admin.register(TypeAllocation)
class TypeAllocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_allocation')
    list_display_links = ('id', 'type_allocation')
    save_on_top = True




@admin.register(FoodType)
class FoodTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'food_type')
    list_display_links = ('id', 'food_type')
    save_on_top = True


@admin.register(Flights)
class FlightsAdmin(admin.ModelAdmin):
    list_display = ('id', 'flight_number', 'city_departure', 'date_departure', 'city_arrival', 'date_arrival')
    list_display_links = ('id', 'flight_number', 'city_departure', 'date_departure', 'city_arrival', 'date_arrival')
    save_on_top = True


@admin.register(Cities)
class CitiesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('city', )}
    list_display = ('id', 'city', 'country', 'get_image')
    list_display_links = ('id', 'city', 'country',)
    save_on_top = True

    def get_image(self, object):
        if object.image:
            return mark_safe(f'<img src="{object.image.url}" width="50">')

    get_image.short_description = 'Миниатюра'


@admin.register(Countries)
class CountriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('country', )}
    list_display = ('id', 'country', 'get_image')
    list_display_links = ('id', 'country',)
    save_on_top = True

    def get_image(self, object):
        if object.image:
            return mark_safe(f'<img src="{object.image.url}" width="50">')

    get_image.short_description = 'Миниатюра'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'tour', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
