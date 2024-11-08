from django.shortcuts import render, get_object_or_404
from .models import Post
from django.urls import reverse
from django.http import HttpResponseRedirect

def list_post(request):
    post_list=Post.objects.all()
    context={'post_list': post_list}
    return render(request, "comidas/index.html",context)

def detail_post(request, post_id):
    post = get_object_or_404(Post,pk=post_id)
    context = {'post': post}
    return render(request, 'comidas/detail.html', context)

def search_post(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        post_list = Post.objects.filter(titulo__icontains=search_term)
        context = {"post_list": post_list}
    return render(request, 'comidas/search.html', context)

def create_post(request):
    if request.method == 'POST':
        post_titulo = request.POST['titulo']
        post_conteudo = request.POST['conteudo']
        post_data = request.POST['data']
        post = Post(titulo=post_titulo, conteudo=post_conteudo,data=post_data)
        post.save()
        return HttpResponseRedirect(
            reverse('comidas:detail', args=(post.id, )))
    else:
        return render(request, 'comidas/create.html', {})
    
def update_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        post.titulo = request.POST['titulo']
        post.conteudo = request.POST['conteudo']
        post.data = request.POST['data']
        post.save()
        return HttpResponseRedirect(
            reverse('comidas:detail', args=(post.id, )))
    context = {'post': post}
    return render(request, 'comidas/update.html', context)

def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        post.delete()
        return HttpResponseRedirect(reverse('comidas:index'))
    context = {'post': post}
    return render(request, 'comidas/delete.html', context)