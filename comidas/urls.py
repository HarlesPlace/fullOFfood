from django.urls import path
from . import views

app_name = 'comidas'
urlpatterns = [
    path('', views.ListView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('search/', views.search_post, name='search'),
    path('update/<int:pk>/', views.UpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.DeleteView.as_view(), name='delete'),
    path('create/', views.CreatView.as_view(), name='create'),
    path('<int:pk>/comment/', views.CommentCreateView.as_view(), name='comment'),
    path('category/', views.categoryListView.as_view(), name='categoryList'),
    path('cetegory/<int:pk>/', views.categoryDetailView.as_view(), name='categoryDetail'),
]