from django import forms
from ExamPrep.mixins import PlaceholderMixin
from profiles.models import Profile


class ProfileBaseForm(PlaceholderMixin, forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'



class ProfileCreateForm(ProfileBaseForm):
    pass