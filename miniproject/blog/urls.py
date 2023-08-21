from django.urls import path
from . import views

urlpatterns = [
    path("", views.BlogListView.as_view(), name="home"),
    path("article/<slug:slug>/", views.BlogDetailView.as_view(), name="article_detail"),
    path("manage/", views.ManageBlogList.as_view(), name="manage_blog_list"),
    path("manage/article/add/", views.AddBlogView.as_view(), name="add_article"),
    path("manage/article/update/<int:pk>/", views.UpdateBlogView.as_view(), name="update_article"),
    path("manage/article/delete/<int:pk>/", views.DeleteBlogView.as_view(), name="delete_article"),
    path("manage/categories/", views.ManageCategoryList.as_view(), name="manage_category_list"),
    path("manage/categories/add/", views.AddCategoryView.as_view(), name="add_category"),
    path("manage/categories/update/<int:pk>/", views.UpdateCategoryView.as_view(), name="update_category"),
    path("manage/categories/delete/<int:pk>/", views.DeleteCategoryView.as_view(), name="delete_category"),
    path("<str:category_name>/", views.BlogListView.as_view(), name="category_detail_list"),
]
