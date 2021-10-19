from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('succulents-details/', views.SucculentDetails.as_view(), name='succulents-details'),
    path('succulents-create/', views.SucculentCreate.as_view(), name='succulents-create'),
    path('succulents-update/<str:pk>/', views.SucculentUpdate.as_view(), name='succulents-update'),
    path('succulents-delete/<str:pk>/', views.SucculentDelete.as_view(), name='succulents-delete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
