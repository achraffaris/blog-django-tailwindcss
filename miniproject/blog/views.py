from django.shortcuts import render
from django.views import generic
from .models import Blog, Category
from django.shortcuts import get_object_or_404
from .forms import BlogForm, CategoryForm
from django.urls import reverse_lazy


class BlogListView(generic.ListView):
    model = Blog
    template_name = 'blog/list.html'
    context_object_name = 'articles'
    paginate_by = 3

    def get_queryset(self):
        category_name = self.kwargs.get('category_name')
        if category_name:
            category = get_object_or_404(Category, slug=category_name)
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
    form_class = BlogForm
    success_url = reverse_lazy('manage_blog_list')
    template_name = 'blog/manage/create.html'


class UpdateBlogView(generic.UpdateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('manage_blog_list')
    template_name = 'blog/manage/update.html'


class DeleteBlogView(generic.DeleteView):
    model = Blog
    template_name = 'blog/manage/delete.html'
    context_object_name = 'article'
    success_url = reverse_lazy('manage_blog_list')


class ManageCategoryList(generic.TemplateView):
    template_name = 'category/manage/list.html'


class AddCategoryView(generic.CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('manage_category_list')
    template_name = 'category/manage/create.html'


class UpdateCategoryView(generic.UpdateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('manage_category_list')
    template_name = 'category/manage/update.html'


class DeleteCategoryView(generic.DeleteView):
    model = Category
    template_name = 'category/manage/delete.html'
    context_object_name = 'category'
    success_url = reverse_lazy('manage_category_list')

def error_404(request, exception):
    context = {
        'error': '404',
        'error_message': 'Page not found'
    }
    return render(request, 'error_page.html', status=404, context=context)

def error_500(request):
    context = {
        'error': '500',
        'error_message': 'Internal server error'
    }
    return render(request, 'error_page.html', status=500, context=context)