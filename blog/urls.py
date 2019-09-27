from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name= 'index'),
    path('detail/', views.detail, name = 'detail'),
    path('category/<int:pk>/', views.category, name = 'category'),
    path('tag/<int:pk>/', views.tag, name = 'tag'),
    path('archives/<int:year>/<int:month>/', views.archives, name = 'archives'),
    path('search/', views.search, name = 'search'),
]