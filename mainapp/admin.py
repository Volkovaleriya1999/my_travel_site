from django.contrib import admin
from .models import News, Category
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms



class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'



@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    prepopulated_fields = {'slug': ('title', )}
    list_display = ('id', 'title', 'get_image', 'created')
    list_display_links = ('id', 'title')
    list_filter = ('cat', 'created')
    search_fields = ('title__iregex', 'content__iregex', 'cat__iregex')
    save_on_top = True

    def get_image(self, object):
        if object.photo:
            return mark_safe(f'<img src="{object.photo.url}" width="50">')

    get_image.short_description = 'Миниатюра'



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
    list_display = ('id', 'name', )
    list_display_links = ('id', 'name', )
    save_on_top = True



# admin.site.register(News)
# admin.site.register(Category)

