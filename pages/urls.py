from django.urls import path
from .views import homepage, blog_detail

urlpatterns = [
    path("", homepage, name="homepage"),
    path("blog_detail/", blog_detail, name="blog_detail"),
]
