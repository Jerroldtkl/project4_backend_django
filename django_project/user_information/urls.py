from django.urls import path
from . import views


urlpatterns = [
    path('profile-list/', views.ProfileList.as_view(), name='profile-list'),
    path('profile-details/<int:id>/', views.ProfileDetails.as_view(), name='profile-details'),
    path('jwt-details/', views.JWTDetails.as_view(), name='jwt-details'),
    path('profile-create/', views.UserCreate.as_view(), name='profile-create'),
    path('profile-update/', views.ProfileUpdate.as_view(), name='profile-update'),

]
