from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.PurchaseList.as_view(), name='purchase-history-list'),
    path('details/<str:pk>/', views.PurchaseDetails.as_view(), name='purchase-history-detail'),
    path('create/', views.PurchaseCreate.as_view(), name='task-create'),
    path('delete/<str:pk>/', views.PurchaseDelete.as_view(), name='purchase-history-delete'),

]
