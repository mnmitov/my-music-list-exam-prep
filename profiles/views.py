from django.views.generic import ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.edit import BaseFormView

from ExamPrep.utils import get_user_obj
from albums.models import Album
from profiles.forms import ProfileCreateForm
from profiles.models import Profile


# Create your views here.
class Home(ListView, BaseFormView):
    model = Album
    form_class = ProfileCreateForm
    success_url = reverse_lazy('home-page')

    def get_template_names(self):
        profile = get_user_obj()

        if profile:
            return ['profile/home-with-profile.html']
        return ['profile/home-no-profile.html']

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        self.object_list = self.get_queryset()
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()  # Add form to context
        return context


class ProfileDetail(DetailView):
    template_name = 'profile/profile-details.html'

    def get_object(self, queryset=None):
        return get_user_obj()


class DeleteDetail(DeleteView):
    template_name = 'profile/profile-delete.html'
    success_url = reverse_lazy('home-page')

    def get_object(self, queryset=None):
        return get_user_obj()
