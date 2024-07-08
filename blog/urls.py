from django.urls import path
from .apps import BlogConfig
from .views import ArticleCreateView, ArticleListView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView


app_name = BlogConfig.name

urlpatterns = [
    path('blog/create/', ArticleCreateView.as_view(), name='blog_create'),
    path('blog/', ArticleListView.as_view(), name='blog_list'),
    path('blog/<int:pk>/', ArticleDetailView.as_view(), name='blog_detail'),
    path('blog/<int:pk>/update/', ArticleUpdateView.as_view(), name='blog_update'),
    path('blog/<int:pk>/delete/', ArticleDeleteView.as_view(), name='blog_delete'),
]