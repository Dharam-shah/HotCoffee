from django.urls import path
from .views import HomepageContent

urlpatterns = [
    path("", HomepageContent.as_view(), name="homepage"),
   # path("blog_detail/", blog_detail, name="blog_detail"),
]
