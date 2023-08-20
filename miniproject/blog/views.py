from django.shortcuts import render
from django.views import generic
from .models import Blog, Category
from django.shortcuts import get_object_or_404

class BlogListView(generic.ListView):
    model = Blog
    template_name = 'blog/list.html'
    context_object_name = 'articles'
    paginate_by = 3

    def get_queryset(self):
        category_name = self.kwargs.get('category_name')
        if category_name:
            category = get_object_or_404(Category, name=category_name)
            return Blog.objects.filter(category=category)
        return Blog.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_name'] = self.kwargs.get('category_name')
        return context

class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = 'blog/detail.html'
    context_object_name = 'article'

class CategoryListView(generic.TemplateView):
    template_name = 'category/manage/list.html'

class ManageBlogList(generic.ListView):
    model = Blog
    template_name = 'blog/manage/list.html'
    context_object_name = 'articles'
    paginate_by = 4

class AddBlogView(generic.CreateView):
    model = Blog
    template_name = 'blog/manage/create.html'