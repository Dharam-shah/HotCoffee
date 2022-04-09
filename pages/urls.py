from django.urls import path
from .views import homepage, blog_detail, Homepage_banner_content

urlpatterns = [
    path("", Homepage_banner_content.as_view(), name="homepage"),
    path("blog_detail/", blog_detail, name="blog_detail"),
]
