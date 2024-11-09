# import for urls
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book_category/', views.book_category_landing, name='book_category'),

    path('sections/', views.book_category, name='book_sections'),

    path('journals/', views.journals, name='journals'),


]