from django.urls import path
from . import views

urlpatterns = [
    path('details/<str:pk>/', views.UsercartDetails.as_view(), name='usercart-detail'),
    path('create/', views.UsercartCreate.as_view(), name='usercart-create'),
    path('update/<str:pk>/', views.UsercartUpdate.as_view(), name='usercart-list'),
    path('delete/<str:pk>/', views.UsercartDelete.as_view(), name='usercart-delete'),
]
