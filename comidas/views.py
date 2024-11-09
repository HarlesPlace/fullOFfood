from django.shortcuts import render, get_object_or_404
from .models import Post
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import PostForm
from django.views import generic

class ListView(generic.ListView):
    model=Post
    template_name='comidas/index.html'

class DetailView(generic.DetailView):
    model=Post
    template_name='comidas/detail.html'

def search_post(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        post_list = Post.objects.filter(titulo__icontains=search_term)
        context = {"post_list": post_list}
    return render(request, 'comidas/search.html', context)

class CreatView(generic.CreateView):
    model= Post
    template_name= 'comidas/create.html'
    form_class=PostForm
    def get_success_url(self):
        return reverse('comidas:detail', args=[self.object.pk])

class UpdateView(generic.UpdateView):
    model= Post
    template_name= 'comidas/update.html'
    form_class=PostForm
    def get_success_url(self):
        return reverse('comidas:detail', args=[self.object.pk])

def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        post.delete()
        return HttpResponseRedirect(reverse('comidas:index'))
    context = {'post': post}
    return render(request, 'comidas/delete.html', context)

class DeleteView(generic.DeleteView):
    model=Post
    template_name='comidas/delete.html'
    def get_success_url(self):
        return reverse('comidas:index')
