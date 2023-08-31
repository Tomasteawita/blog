from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.db.models import Prefetch
from django.views.generic import ListView, View
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView
)
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy

class IndexView(ListView):
    template_name = 'index.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(user_id = self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    