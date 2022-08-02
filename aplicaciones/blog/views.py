from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Post, Categoria



# Create your views here.
def home(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(estado=True).order_by('id')
    if queryset:
        posts = posts.filter(
            Q(titulo__icontains=queryset) |
            Q(descripcion__icontains=queryset)
        ).distinct()

    """ Paginacion """
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    paginas = paginator.count

    return render(request, 'index.html', {'posts': posts, 'paginas': paginas})


def generales(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(
        estado=True,
        categoria=Categoria.objects.get(nombre__iexact='Generales')
    ).order_by('id')
    if queryset:
        posts = posts.filter(
            Q(titulo__icontains=queryset) |
            Q(descripcion__icontains=queryset)
        ).distinct()

    """ Paginacion """
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    paginas = paginator.count

    return render(request, 'generales.html', {'posts': posts, 'paginas': paginas})


def tecnologia(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(
        estado=True,
        categoria=Categoria.objects.get(nombre__iexact='Tecnología')
    ).order_by('id')
    if queryset:
        posts = posts.filter(
            Q(titulo__icontains=queryset) |
            Q(descripcion__icontains=queryset)
        ).distinct()

    """ Paginacion """
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'tecnologia.html', {'posts': posts})


def videojuegos(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(
        estado=True,
        categoria=Categoria.objects.get(nombre__iexact='Videojuegos')
    ).order_by('id')
    if queryset:
        posts = posts.filter(
            Q(titulo__icontains=queryset) |
            Q(descripcion__icontains=queryset)
        ).distinct()

    """ Paginacion """
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'videojuegos.html', {'posts': posts})


def espacio(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(
        estado=True,
        categoria=Categoria.objects.get(nombre__iexact='Espacio')
    ).order_by('id')
    if queryset:
        posts = posts.filter(
            Q(titulo__icontains=queryset) |
            Q(descripcion__icontains=queryset)
        ).distinct()

    """ Paginacion """
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'espacio.html', {'posts': posts})


def detallePost(request, slug):
    post = get_object_or_404(Post, slug=slug)
    # post = Post.objects.get(slug=slug)
    # print(post)
    return render(request, 'post.html', {'detalle_post': post})
