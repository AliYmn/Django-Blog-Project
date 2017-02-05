from django.contrib import admin
from .models import Category,Post,SiteInfo


class PostModel(admin.ModelAdmin):
    exclude = ('url',)
    list_display = ('title','url','time','category_list','is_active','image')
    search_fields = ('title', 'content','is_active',)
    list_editable = ('category_list', 'is_active','image')
    list_filter = (
        ('is_active', admin.BooleanFieldListFilter),
    )

class CategoryModel(admin.ModelAdmin):
    list_display = ('title','url','description','parent')
    list_editable = ('description','parent')
    search_fields = ('title', 'url','description',)
    exclude = ('url',)
    list_filter = ('title',)

class SiteModel(admin.ModelAdmin):
    list_display = ('title','slogan','author','image')
    search_fields = ('title', 'slogan','description',)


admin.site.register(Category,CategoryModel)
admin.site.register(Post,PostModel)
admin.site.register(SiteInfo,SiteModel)

