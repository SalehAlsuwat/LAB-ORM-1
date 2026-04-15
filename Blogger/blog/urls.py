from . import views
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('add/', views.add_post_view, name='add_post_view'),
    path('post/<post_id>/', views.detail_post_view, name='detail_post_view'),
    path('post/<post_id>/update/', views.update_post_view, name='update_post_view'),
    path('post/<post_id>/delete/', views.delete_post_view, name='delete_post_view'),
]