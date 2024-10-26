from django.urls import path
from profiles.views import DeleteDetail, ProfileDetail

urlpatterns = [
    path('details/', ProfileDetail.as_view(), name='profile-detail'),
    path('delete/', DeleteDetail.as_view(), name='delete-profile')
]