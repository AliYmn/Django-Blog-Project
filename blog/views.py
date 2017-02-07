from django.views.generic import ListView,TemplateView,DetailView,View
from .models import Post,Category,Love,Skills,IpController

class HomeListView(ListView):

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
    model = Post
    template_name = 'post.html'
    context_object_name = 'post_obj'
    slug_field = 'url'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['last_content'] = Post.objects.all().filter(is_active=True).order_by('-time')[:5]
        context['category'] = Category.objects.all()
        context['post'] = Post.objects.all().filter(is_active=True).order_by('-site_hit')[:5]
        ip = IpController.objects.all().filter(remote=str(self.request.META.get('REMOTE_ADDR')),http_x=str(self.request.META.get('HTTP_X_FORWARDED_FOR')),
                                    http_user=str(self.request.META['HTTP_USER_AGENT']),url=str(self.kwargs['slug']))
        if(not ip):
            IpController.objects.create(remote=str(self.request.META.get('REMOTE_ADDR')),http_x=str(self.request.META.get('HTTP_X_FORWARDED_FOR')),
                                    http_user=str(self.request.META['HTTP_USER_AGENT']),url=str(self.kwargs['slug'])).save()

            hit = Post.objects.get(url=self.kwargs['slug'])
            hit.site_hit += 1
            hit.save()

        return context

class AboutTemplateView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutTemplateView, self).get_context_data(**kwargs)
        context['last_content'] = Post.objects.all().filter(is_active=True).order_by('-time')
        context['love'] = Love.objects.all()
        context['skills'] = Skills.objects.all().order_by()
        return context

class BlogListView(ListView):
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
        return context

class ContactView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['last_content'] = Post.objects.all().filter(is_active=True).order_by('-time')
        return context

class CategoryView(ListView):
        model = Post
        template_name = 'category_page.html'
        context_object_name = 'post_obj'
        paginate_by = 3
        def get_queryset(self, *args, **kwargs):
            return Post.objects.filter(category_list__url=self.kwargs['slug'],is_active=True)

        def get_context_data(self, **kwargs):
            context = super(CategoryView, self).get_context_data(**kwargs)
            context['last_content'] = Post.objects.all().filter(is_active=True).order_by('-time')
            context['category'] = Category.objects.all()
            context['category_post'] = Category.objects.all().filter(url=self.kwargs['slug'])
            return context

class RobotsView(TemplateView):
    template_name = 'robots.html'