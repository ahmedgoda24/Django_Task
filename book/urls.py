from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter
from book.api import api_views
router = DefaultRouter()
router.register('books', api_views.BookViewSet, basename='books')


urlpatterns = [
    path("api/",include(router.urls )),
    path('', views.BookListView.as_view(), name='book_list'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('book/new/', views.book_create, name='book_create'),
    path('book/<int:pk>/edit/', views.book_update, name='book_update'),
    path('book/<int:pk>/delete/', views.book_delete, name='book_delete'),
    path('page/', views.multiplication_table, name='multiplication_table'),
]
