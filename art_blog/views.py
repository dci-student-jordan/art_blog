from typing import Any
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["MEDIA_URL"] = settings.MEDIA_URL
        return context


class DataDetailsView(DetailView):
    model = Item
    template_name = "data_details.html"
    context_object_name = "item"

    def post(self, request, *args, **kwargs):
        # Handling comment submission
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user_fname = request.user
            comment.item = self.get_object()
            comment.save()
            return redirect(self.request.path_info)

        # Handling voting action
        if 'vote' in request.POST:
            item = self.get_object()
            item.vote(request.user)
            return redirect(self.request.path_info)

        return super().post(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        item = self.get_object()
        context["comments"] = Comment.objects.filter(item=item)
        context["MEDIA_URL"] = settings.MEDIA_URL
        context["comment_form"] = CommentForm()
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
