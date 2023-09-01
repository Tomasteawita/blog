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

class IndexView(View):
    template_name = 'index.html'

    def get(self, request):
        tag_id = request.GET.get('tag_id')
        
        # Obtener todos los tags únicos relacionados con los posts
        show_tag_buttons = Tag.objects.filter(post__isnull=False).distinct()

        if tag_id:
            posts = Post.objects.filter(tags__id=tag_id)
        else:
            posts = Post.objects.all()

        return render(request, self.template_name, {'posts': posts, 'show_tag_buttons': show_tag_buttons})



