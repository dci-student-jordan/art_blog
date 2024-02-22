from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from .forms import CommentForm
from .models import Comment
from art_api.models import ArtWork as Item
from django.conf import settings


class MainPageView(TemplateView):
    template_name = "main_page.html"


class DataListView(ListView):
    model = Item
    template_name = "data_list.html"
    context_object_name = "items"


class DataDetailsView(DetailView):
    model = Item
    template_name = "data_details.html"
    context_object_name = "item"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        item = self.get_object()
        context["comments"] = Comment.objects.filter(item=item)
        context["MEDIA_URL"] = settings.MEDIA_URL
        return context


class CommentView(TemplateView):
    template_name = "comment_box.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()  # Save the comment to the database
            return redirect("comment_success")  # Redirect to a success page
        else:
            return render(request, self.template_name, {"form": form})
