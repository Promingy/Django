from django.urls import path
# from .views import article_list_view, article_create_view, article_detail_view
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleUpdateView,
    ArticleCreateView,
    ArticleDeleteView
)

app_name="blog"

urlpatterns = [
    path("", ArticleListView.as_view(), name="list-view"),
    path("<int:pk>/", ArticleDetailView.as_view(), name="article-detail"),
    path("create/", ArticleCreateView.as_view(), name="article-create"),
    path("<int:pk>/update/", ArticleUpdateView.as_view(), name="article-update"),
    path("<int:pk>/delete", ArticleDeleteView.as_view(), name="article-delete")

    # path("", article_list_view, name="list-view"),
    # path("create/", article_create_view, name="article-create"),
    # path("<int:id>/", article_detail_view, name="article-detail"),
]