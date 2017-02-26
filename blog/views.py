from django.views.generic import ListView,TemplateView,DetailView
from .models import Post,Category,Love,Skills,IpController,Tags
from django.shortcuts import get_list_or_404
from django.contrib.syndication.views import Feed
from django.urls import reverse
from django.contrib.sites.models import Site

class HomeListView(ListView):
    """Ana Sayfa"""
    model = Post
    queryset = Post.objects.all().filter(is_active=True).order_by('?')
    context_object_name = 'post_obj'
    template_name = 'home.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        context['last_content'] = Post.objects.all().filter(is_active=True).order_by('-time')
        return context


class PostDetailView(DetailView):
    """Post detay sayfası"""
    model = Post
    template_name = 'post.html'
    context_object_name = 'post_obj'
    slug_field = 'url'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['last_content'] = Post.objects.all().filter(is_active=True).order_by('-time')[:5]
        context['category'] = Category.objects.all()
        context['post'] = Post.objects.all().filter(is_active=True).order_by('-site_hit')[:5]

        ip = IpController.objects.all().filter(remote=str(self.request.META.get('REMOTE_ADDR')),
                                               http_x=str(self.request.META.get('HTTP_X_FORWARDED_FOR')),
                                               http_user=str(self.request.META['HTTP_USER_AGENT']),
                                               url=str(self.kwargs['slug']))
        if(ip):
            """Kullanıcı siteyi görüntülenmiş. Tekrar hit saymıyoruz."""
            pass
        else:
            IpController.objects.create(remote=str(self.request.META.get('REMOTE_ADDR')),
                                        http_x=str(self.request.META.get('HTTP_X_FORWARDED_FOR')),
                                        http_user=str(self.request.META['HTTP_USER_AGENT']),
                                        url=str(self.kwargs['slug'])).save()

            hit = Post.objects.get(url=self.kwargs['slug'])
            hit.site_hit += 1
            hit.save()

        return context

class AboutTemplateView(TemplateView):
    """Hakkımızda"""
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutTemplateView, self).get_context_data(**kwargs)
        context['last_content'] = Post.objects.all().filter(is_active=True).order_by('-time')
        context['love'] = Love.objects.all()
        context['skills'] = Skills.objects.all().order_by()
        return context

class BlogListView(ListView):
    """Blog Listeleme"""
    model = Post
    queryset = Post.objects.all().filter(is_active=True).order_by('-time')
    context_object_name = 'post_obj'
    template_name = 'blog_list.html'
    paginate_by = 5


    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        context['last_content'] = Post.objects.all().filter(is_active=True).order_by('-time')
        context['category'] = Category.objects.all()
        context['post'] = Post.objects.all().filter(is_active=True).order_by('-site_hit')[:5]
        context['random_post'] = Post.objects.all().filter(is_active=True).order_by('?')
        return context

class ContactView(TemplateView):
    """İletişim"""
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['last_content'] = Post.objects.all().filter(is_active=True).order_by('-time')
        return context

class CategoryView(ListView):
    """Kategori Detay"""
    model = Post
    template_name = 'category_page.html'
    context_object_name = 'post_obj'
    paginate_by = 3
    def get_queryset(self, *args, **kwargs):
        return get_list_or_404(Post.objects.filter(category_list__url=self.kwargs['slug'],is_active=True))

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['last_content'] = Post.objects.all().filter(is_active=True).order_by('-time')
        context['category'] = Category.objects.all()
        context['category_post'] = Category.objects.all().filter(url=self.kwargs['slug'])
        return context

class RobotsView(TemplateView):
    """robots.txt"""
    template_name = 'robots.html'

    def get_context_data(self, **kwargs):
        context = super(RobotsView, self).get_context_data(**kwargs)
        context['domain'] =  current_site = Site.objects.get_current().domain
        return context



class TagsView(ListView):
    """etiket detay"""
    model = Tags
    context_object_name = 'tags_obj'
    template_name = 'tags.html'
    paginate_by = 5

    def get_queryset(self):
        return get_list_or_404(Tags.objects.all().filter(blog__is_active=True,tags=self.kwargs['slug']))

    def get_context_data(self, **kwargs):
        context = super(TagsView, self).get_context_data(**kwargs)
        context['last_content'] = Post.objects.all().filter(is_active=True).order_by('-time')
        context['category'] = Category.objects.all()
        context['tags'] = Tags.objects.all().filter(blog__is_active=True,tags=self.kwargs['slug'])[:1]
        return context



class LatestEntriesFeed(Feed):
    """Feed"""
    title = "Feeds"
    link = "/sitenews/"
    description = "Kişisel Blog"

    def items(self):
        return Post.objects.order_by('-time')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse('post', args=[item.url])
