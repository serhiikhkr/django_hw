from django.urls import path

from . import views

app_name = 'quotes'

urlpatterns = [
    path('', views.main, name='root'),
    path('<int:page>', views.main, name='root_paginate'),
    path('author/<str:author_id>/', views.author_detail, name='author_detail'),
    path('authornew/', views.create_author, name='author_create'),
    path('quotenew/', views.create_quote, name='quote_create'),
]