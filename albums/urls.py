from django.urls import path
from albums import views

urlpatterns = [
    path('add/', views.AddAlbum.as_view(), name='add-album'),
    path('<int:id>/details/', views.AlbumDetails.as_view(), name='album-details'),
    path('<int:id>/edit/', views.EditAlbum.as_view(), name='edit-album'),
    path('<int:id>/delete/', views.DeleteAlbum.as_view(), name='delete-album')
]