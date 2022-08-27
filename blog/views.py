from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import PostForm

from .models import Post, Comments
from .forms import CommentForm


# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    print(posts.query)
    return render(request, 'blog/blog_list.html', {'posts': posts})


def post_create(request):
    # si es una petición get, es decir, si se visita la 
    # página de creación de post por primera vez
    form = PostForm() # instanciamos el formulario sin datos previos
    if request.method == 'POST':
        # si es una petición post, es decir, el usuario rellenó los campos
        # del formulario
        # cargamos los datos enviados por petición post al formulario
        # acá, de esta manera, notar que como tiene campo con archivos, esos van en request.FILES
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # si es válido el formulario creamos el objeto post pero no lo guardamos en db: commit=False
            post = form.save(commit=False)
            post.user = request.user # asignamos el autor del post
            post.save() # guardamos
            messages.success(request, 'Post creado con éxito') # mandamos un mensaje de éxito
            return redirect('post_list') # dirigimos al usuario a la página que nos parezca
        messages.error(request, 'Hay errores en el formulario')
    return render(request, 'blog/blog_create.html', {'form': form})


def post_update(request, pk):
    # recibimos ese argumento 'pk' enviado como parte de la url:
    # path('update/<int:pk>/', views.post_update, name='post_update'), es pk es el que recibimos como argumento
    post = get_object_or_404(Post, id=pk) # buscamos el post o devolvemos un 404 (not found)

    # instanciamos el formulario e inicializamos los campos con los datos del post encontrado (instance=post)
    form = PostForm(instance=post)
    if request.method == 'POST':
        # si es una petición post, es decir, el usuario está guardando el formulario
        # rellenamos con los datos en POST y FILES
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            # si es válido, guardamos el formulario, se guarda la instancia, de hecho
            form.save()
            return redirect('post_list') # redirigimos
    return render(request, 'blog/blog_update.html', {'form': form, 'post': post})

def post_delete(request, pk):
    # buscamos el post y lo borramos, lanzamos un error 404 (Not found caso contrario)
    post = get_object_or_404(Post, id=pk)
    post.delete()
    return redirect('post_list')


def post_detail(request, pk):
    # buscamos el post y lo mostramos
    post = get_object_or_404(Post, id=pk)
    post.views_number += 1
    post.save()
    return render(request, 'blog/blog_detail.html', {'post': post})

def comment_create(request, pk):
    # buscamos el post y lo mostramos
    context = {}
    post = get_object_or_404(Post, id=pk)
    form = CommentForm()
    context['post'] = post
    context['form'] = form
    if request.method == 'POST':
        form = CommentForm(request.POST)
        context['form'] = form
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)
    return render(request, 'blog/comment_create.html', context)

def comment_delete(request, pk):
    comment = get_object_or_404(Comments, id=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)

def comment_update(request, pk):
    # buscamos el post y lo mostramos
    # context = {}
    comment = get_object_or_404(Comments, id=pk)
    form = CommentForm(request.POST or None, instance=comment)
    context = {
        'comment': comment,
        'post': comment.post,
        'form': form,
    }
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=comment.post.pk)
    return render(request, 'blog/comment_edit.html', context)
