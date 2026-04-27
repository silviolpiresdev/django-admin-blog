from django.urls import path
from .views import PostListView, PostDetailView

urlpatterns = [
    path("posts", PostListView.as_view(), name="lista_posts"),
    path("post/<int:pk>", PostDetailView.as_view(), name="lista_post")
]