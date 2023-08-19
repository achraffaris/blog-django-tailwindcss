from django.urls import path
from . import views

urlpatterns = [
    path("", views.BlogListView.as_view(), name="home"),
    path("article/<slug:slug>/", views.BlogDetailView.as_view(), name="blog_detail"),
    path("categories/", views.CategoryListView.as_view(), name="category_list"),
    path("<str:category_name>/", views.BlogListView.as_view(), name="category_detail_list"),

]
