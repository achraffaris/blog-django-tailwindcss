from django.shortcuts import render
from django.views import generic
from .models import Blog, Category

class BlogListView(generic.ListView):
    model = Blog
    template_name = 'blog/main.html'
    context_object_name = 'articles'
    paginate_by = 6

    def get_queryset(self):
        category_name = self.kwargs.get('category_name')
        if category_name:
            return Blog.objects.filter(category__name=category_name)
        return Blog.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_name'] = self.kwargs.get('category_name')
        return context

class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = 'blog/detail.html'
    context_object_name = 'article'

class CategoryListView(generic.ListView):
    model = Category
    template_name = 'category/list.html'
    context_object_name = 'categories'