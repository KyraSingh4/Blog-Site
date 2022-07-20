from django.urls import path
from .views import (
	PostListView, 
	PostDetailView,
	PostCreateView,
	PostUpdateView,
	PostDeleteView,
	UserPostListView
)
from . import views

urlpatterns = [
	path('', views.PostListView.as_view(), name = 'blog-home'),
	path('user/<str:username>', views.UserPostListView.as_view(), name = 'user-posts'),
	path('post/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'), # 'admin/' to '' so we don't have to type anything in url -- home.html home path (blog-home)
	path('post/new/', PostCreateView.as_view(), name = 'post-create'),
	path('post/<int:pk>/update/', PostUpdateView.as_view(), name = 'post-update'),
	path('post/<int:pk>/delete/', PostDeleteView.as_view(), name = 'post-delete'),
	path('about/', views.about, name = 'blog-about'),
	path('more/', views.more, name = 'blog-more')
]


# looking for a template with <app>/<model>_<viewtype>.html
# looking for blog/post_list/html

