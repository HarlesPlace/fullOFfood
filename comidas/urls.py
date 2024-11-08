from django.urls import path
from . import views

app_name = 'comidas'
urlpatterns = [
    path('', views.list_post, name='index'),
    path('<int:post_id>/', views.detail_post, name='detail'),
    path('search/', views.search_post, name='search'),
    path('update/<int:post_id>/', views.update_post, name='update'),
    path('delete/<int:post_id>/', views.delete_post, name='delete'),
    path('create/', views.create_post, name='create'),
]