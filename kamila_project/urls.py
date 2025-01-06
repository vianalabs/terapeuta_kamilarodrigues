from django.contrib import admin
from django.urls import path

from app import views
from django.urls import include, path

urlpatterns = [
    path("post/", views.post, name="post"),
    path("blog/", views.blog, name="blog"),
    path("index/", views.index, name="index"),
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("__reload__/", include("django_browser_reload.urls")),
]
