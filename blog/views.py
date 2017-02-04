from django.shortcuts import render
from django.views.generic import ListView,TemplateView,DetailView

from .models import Post,Category
# Create your views here.



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
        context['last_content'] = Post.objects.all().filter(is_active=True).order_by('-time')
        context['category'] = Category.objects.all()
        return context

class AboutTemplateView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutTemplateView, self).get_context_data(**kwargs)
        context['last_content'] = Post.objects.all().filter(is_active=True).order_by('-time')
        return context

class BlogListView(ListView):
    model = Post
    queryset = Post.objects.all().filter(is_active=True).order_by('-time')
    context_object_name = 'post_obj'
    template_name = 'blog_list.html'
     = 5

    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        context['last_content'] = Post.objects.all().filter(is_active=True).order_by('-time')
        context['category'] = Category.objects.all()
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
            return Post.objects.filter(category_list__title=self.kwargs['slug'])

        def get_context_data(self, **kwargs):
            context = super(CategoryView, self).get_context_data(**kwargs)
            context['last_content'] = Post.objects.all().filter(is_active=True).order_by('-time')
            context['category'] = Category.objects.all()
            context['category_post'] = Category.objects.all().filter(title=self.kwargs['slug'])
            return context


