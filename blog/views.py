from django.shortcuts import render
from .forms import *
from .models import *
from django.views.generic import View
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView
)
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

class IndexView(View):
    """
    Vista basada en clase para la página de inicio.
    Esta vista muestra una lista de posts y etiquetas únicas relacionadas con los posts.
    Attributes:
        template_name (str): El nombre de la plantilla HTML a utilizar para renderizar la página.

    Methods:
        get(self, request): Procesa una solicitud GET para mostrar la página de inicio.
    """
    template_name = 'index.html'

    def get(self, request):
        """
        Procesa una solicitud GET para mostrar la página de inicio.
        Esta función recibe una solicitud GET, procesa los parámetros de consulta para filtrar
        posts por etiqueta si se proporciona 'tag_id', y luego renderiza la página de inicio.
        
        Args:
            request (HttpRequest): La solicitud HTTP enviada por el usuario.

        Returns:
            HttpResponse: Una respuesta HTTP que representa la página de inicio con los posts y
                          etiquetas únicas relacionadas con los posts.
        """
        tag_id = request.GET.get('tag_id')
        
        show_tag_buttons = Tag.objects.filter(post__isnull=False).distinct()

        if tag_id:
            posts = Post.objects.filter(tags__id=tag_id)
        else:
            posts = Post.objects.all()

        return render(request, self.template_name, {'posts': posts, 'show_tag_buttons': show_tag_buttons})

class CreatePostView(CreateView):
    model = Post
    template_name = 'crud_posts/cu_post.html'
    form_class = PostForm
    
    def get_success_url(self):
        return reverse('TransactionCompleted')

class DeletePostView(DeleteView):
    model = Post
    template_name = 'crud_posts/d_post.html'
    
    def get_success_url(self):
        return reverse('TransactionCompleted')
    
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        
        return render(request, self.template_name, {'post': post})

class EditPostView(UpdateView):
    model = Post
    template_name = 'crud_posts/cu_post.html'
    form_class = PostForm
    
    def get_success_url(self):
        return reverse('TransactionCompleted')

class DetailPostView(View):
    template_name = 'crud_posts/r_post.html'
    
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        
        return render(request, self.template_name, {'post': post})


def transaction_completed_view(request):
    return render(request, 'crud_posts/transaction_completed.html')