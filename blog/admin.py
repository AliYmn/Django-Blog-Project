from django.contrib import admin
from .models import Category,Post,SiteInfo,Love,Skills,Tags,IpController

class TagsInline(admin.TabularInline):
    model = Tags
    extra = 0

class PostModel(admin.ModelAdmin):
    exclude = ('url','ip',)
    list_display = ('title','url','time','category_list','is_active','image','site_hit')
    search_fields = ('title', 'content','is_active',)
    list_editable = ('category_list', 'is_active','image')
    list_filter = (
        ('is_active', admin.BooleanFieldListFilter),
    )
    inlines= [
        TagsInline,
    ]

class CategoryModel(admin.ModelAdmin):
    list_display = ('title','url','description','parent')
    list_editable = ('description','parent')
    search_fields = ('title', 'url','description',)
    exclude = ('url',)
    list_filter = ('title',)

class SiteModel(admin.ModelAdmin):
    list_display = ('title','slogan','author','image')
    search_fields = ('title', 'slogan','description',)

class LoveModel(admin.ModelAdmin):
    list_display = ('icon','description')
    search_fields = ('icon','description',)

class SkillsModel(admin.ModelAdmin):
    list_display = ('title','rate')
    search_fields = ('title','rate',)

admin.site.register(Category,CategoryModel)
admin.site.register(Post,PostModel)
admin.site.register(SiteInfo,SiteModel)
admin.site.register(Love,LoveModel)
admin.site.register(Skills,SkillsModel)
admin.site.register(Tags)
admin.site.register(IpController)