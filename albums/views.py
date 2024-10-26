from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView, DetailView, CreateView

from ExamPrep.utils import get_user_obj
from albums.forms import AlbumCreateForm, AlbumEditForm, AlbumDeleteForm
from albums.models import Album

# Create your views here.


class AlbumDetails(DetailView):
    model = Album
    pk_url_kwarg = 'id'
    template_name = 'albums/album-details.html'


class AddAlbum(CreateView):
    model = Album
    form_class = AlbumCreateForm
    template_name = 'albums/album-add.html'
    success_url = reverse_lazy('home-page')

    def form_valid(self, form):
        form.instance.owner = get_user_obj()
        return super().form_valid(form)


class EditAlbum(UpdateView):
    model = Album
    form_class = AlbumEditForm
    template_name = 'albums/album-edit.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home-page')


class DeleteAlbum(DeleteView):
    model = Album
    form_class = AlbumDeleteForm
    template_name = 'albums/album-delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home-page')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)
