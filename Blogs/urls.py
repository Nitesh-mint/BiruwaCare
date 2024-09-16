from django.urls import path

from .views import PostListView, PostDetailView

urlpatterns = [
   path('post/', PostListView.as_view(), name="post_list"),
   path('post/<slug:slug>/', PostDetailView.as_view(), name="post_detail")
]