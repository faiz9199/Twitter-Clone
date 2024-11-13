
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.tweet_list_view, name='tweet_list_view'),
    path('tweet/', views.tweet_create_view, name='tweet-create'),
    path('tweet/edit/<int:pk>/', views.tweet_edit_view, name='tweet-edit'),
    path('tweet/delete/<int:pk>/', views.tweet_delete_view, name='tweet-delete'),
    path('tweet/like/<int:pk>/', views.like_tweet_view, name='like_tweet_view'),
    path('register', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='tweet/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='tweet_list_view'), name='logout'),
]
