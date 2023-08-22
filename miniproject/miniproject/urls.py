from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500
from blog import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('blog.urls'))
]

handler404 = views.error_404
handler500 = views.error_500