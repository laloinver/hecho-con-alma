from django.urls import path

from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('add/', views.post_create, name='post_create'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('<int:pk>/update/', views.post_update, name='post_update'),
    path('<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('<int:pk>/comments/add/', views.comment_create, name='comment_create'),
    path('comments/<int:pk>/delete/', views.comment_delete, name='comment_delete'),
    path('comments/<int:pk>/edit/', views.comment_update, name='comment_update'),
    path('category/add/', views.category_create, name='category_create'),
    path('category/<slug:any>', views.category_detail, name='category_detail'),
]
