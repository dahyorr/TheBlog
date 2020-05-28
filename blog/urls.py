from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
    path('', views.PostListView.as_view(), name='Home'),
    path('about/', views.AboutView.as_view(), name='About'),
    path('post/view/<pk>/', views.PostDetailView.as_view(), name='Post Detail'),
    path('post/new/', views.CreatePostView.as_view(), name='New Post'),
    path('post/<pk>/edit/', views.PostUpdateView.as_view(), name='Post Edit'),
    path('post/<pk>/delete/', views.PostDeleteView.as_view(), name='Post Delete'),
    path('post/<pk>/publish/', views.post_publish, name='Post Publish'),
    path('post/drafts/', views.DraftListView.as_view(), name='Post Drafts List'),
    path('post/<pk>/comment/', views.add_comments_to_post, name='Post Comment'),
    path('comment/<pk>/approve/', views.comment_approve, name='Comment Approve'),
    path('comment/<pk>/delete/', views.comment_remove, name='Comment Delete'),


]
