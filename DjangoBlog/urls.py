"""DjangoBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from blog.views import (HomeListView,PostDetailView,
                        AboutTemplateView,BlogListView,
                        ContactView,CategoryView,RobotsView,TagsView,LatestEntriesFeed)
from django.conf import settings
from django.views.static import serve
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from blog.models import Post,Category,Tags

post_dict = {
    'queryset': Post.objects.all(),
    'date_field': 'time',
}

category_dict = {
    'queryset':Category.objects.all(),
}

tags_dict = {
    'queryset':Tags.objects.all(),
}

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeListView.as_view(),name="home-list"),
    url(r'^hakkimda/', AboutTemplateView.as_view(), name="about"),
    url(r'^iletisim/', ContactView.as_view(), name="about"),
    url(r'^blog/', BlogListView.as_view(), name="about"),
    url(r'^kategori/(?P<slug>[-\w]+)/', CategoryView.as_view(), name='list-detail'),
    url(r'^etiket/(?P<slug>[-\w]+)/$', TagsView.as_view(), name='tags'),

    url(r'^sitemap_post\.xml$', sitemap,{'sitemaps': {'blog': GenericSitemap(post_dict, priority=0.6)}},
                                                 name='django.contrib.sitemaps.views.sitemap'),

    url(r'^sitemap_category\.xml$', sitemap,{'sitemaps': {'blog': GenericSitemap(category_dict, priority=0.6)}},
                                                 name='django.contrib.sitemaps.views.sitemap'),

    url(r'^sitemap_tags\.xml$', sitemap, {'sitemaps': {'blog': GenericSitemap(tags_dict, priority=0.6)}},
        name='django.contrib.sitemaps.views.sitemap'),

    url(r'^robots.txt/', RobotsView.as_view(), name="robots"),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

    url(r'^feed/$', LatestEntriesFeed()),
    url(r'^(?P<slug>[-\w]+)/$', PostDetailView.as_view(), name='post'),

]

urlpatterns += [
url(r'^media/(?P<path>.*)$', serve, {
    'document_root': settings.MEDIA_ROOT,
}),
]