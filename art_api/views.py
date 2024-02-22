from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import RegisterArtistForm, RegisterUserForm

# Create your views here.

class CreateArtistView(FormView):
    template_name = "registration/register_artist.html"
    form_class = RegisterArtistForm
    success_url = reverse_lazy('art_blog:main_page')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_staff = True
        user.save()
        return super().form_valid(form)



class CreateUserView(FormView):
    template_name = "registration/register_user.html"
    form_class = RegisterUserForm
    success_url = reverse_lazy('art_blog:main_page')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)