from django.urls import path
from . import views

urlpatterns = [
    path('profile-list/', views.ProfileList.as_view(), name='profile-list'),
    path('profile-details/', views.ProfileDetails.as_view(), name='profile-details'),
    path('profile-create/', views.ProfileCreate.as_view(), name='profile-create'),
    path('profile-update/', views.ProfileUpdate.as_view(), name='profile-update'),

]
