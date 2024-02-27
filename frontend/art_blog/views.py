from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from .forms import CommentForm
from .models import Comment, Vote
from art_shop.models import Selledartwork, ArtworkToSell
from django.conf import settings
import requests
import json


class MainPageView(TemplateView):
    template_name = "main_page.html"


class DataListView(TemplateView):
    template_name = "data_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        artwork_list_url = settings.ART_API_URL+"artwork/"
        response = requests.get(artwork_list_url)
        list_json = response.json()
        context["items"] = list_json
        return context


class DataDetailsView(TemplateView):
    template_name = "data_details.html"
    context_object_name = "item"

    def post(self, request, *args, **kwargs):
        # Handling comment submission
        form = CommentForm(request.POST)
        pk = kwargs["pk"]
        print("PK:", pk)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user_fname = request.user
            comment.item = pk
            comment.save()
            return redirect(self.request.path_info)

        # Handling voting action
        if 'vote' in request.POST:
            if self.request.user.pk in Vote.objects.filter(item=pk).values_list("user", flat=True):
                existing_vote = Vote.objects.filter(item=pk, user=self.request.user.pk).first()
                if existing_vote:
                    existing_vote.delete()
            else:
                Vote.objects.create(item=pk, user=self.request.user)
            return redirect(self.request.path_info)

        return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = kwargs["pk"]
        artwork_list_url = settings.ART_API_URL+"artwork/"+str(pk)
        response = requests.get(artwork_list_url)
        item = response.json()
        context["item"] = item
        is_sold = Selledartwork.objects.filter(item=pk).exists()
        if is_sold:
            context["price"] = Selledartwork.objects.filter(item=pk).values_list("price", flat=True).first()
        else:
            context["price"] = ArtworkToSell.objects.filter(item=pk).values_list("price", flat=True).first()
        context["is_sold"] = is_sold
        context["voters"] = Vote.objects.filter(item=pk)
        vote_users = Vote.objects.filter(item=pk).values_list("user", flat=True)
        context["did_vote"] = self.request.user.pk in vote_users
        context["comments"] = Comment.objects.filter(item=pk)
        context["comment_form"] = CommentForm()
        return context


class CommentView(TemplateView):
    # template_name = "comment_box.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["form"] = CommentForm()
    #     return context

    # def post(self, request, *args, **kwargs):
    #     form = CommentForm(request.POST)
    #     if form.is_valid():
    #         comment = form.save()  # Save the comment to the database
    #         return redirect("comment_success")  # Redirect to a success page
    #     else:
    #         return render(request, self.template_name, {"form": form})
    pass